from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import login as auth_login
from django.db.models.signals import pre_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from .models import Product
from .models import Order
from django.core.exceptions import ObjectDoesNotExist
from proteinzApp.middlewares.auth import auth_middleware
from .models import Categories
from .models import Customer
from django.db.models import Q    #for using multiple filters at one go


User = get_user_model()


def product_detail(request, product_id):
    # Retrieve the product details using the product_id
    product = get_object_or_404(Product, pk=product_id)

    # Render the product detail page with the selected product
    return render(request, 'product_detail.html', {'product': product})

def cart (request):
    prds=None
    category_ID = request.GET.get('Categories')
    if category_ID:
        prds=Product.get_products_category_id(category_ID)
    else:
        prds=Product.get_products
    # prds=Product.get_products_category_id(category_id=3)    product from specific category id
    return render (request,'cart.html', {'product':prds})  # don't forget to put your templates in same folder of the project

def checkout (request):
    if request.method == "POST":
        #print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_name = request.session.get('customer_name')
        cart = request.session.get('cart')
        if not cart:  # Check if the cart is empty
            return redirect('login')
        products = Product.get_products_by_ids(list(cart.keys()))
        try:
            customer = Customer.objects.get(full_name=customer_name)
        except ObjectDoesNotExist:
            # Handle case when customer does not exist
            return redirect('login')
        for product in products:
            order = Order(customer =customer,
                          customer_name=customer_name,
                          product_name=product.name,
                          product = product,
                          price = product.price,
                          quantity = cart.get(str(product.id)),
                          address = address,
                          phone = phone)
            order.save()
        request.session['cart'] = {}                              #to empty cart after clicking checkout button
       # print(address,phone,customer,products,cart)
        return redirect ('cart')
         
    else:
        return redirect ('cart')   
     
@auth_middleware
def orders(request):
     if request.method == "GET":
        customer_name = request.session.get('customer_name')
        customer = Customer.objects.get(full_name=customer_name)
        orders = Order.get_orders_by_customer(customer)
        #print(orders)
        orders = orders.reverse()        #so we can get the list according to date i.e latest cart item added

        return render (request,'orders.html',{'orders':orders})


def inde (request):
    
    if request.method == "GET":
        cart=request.session.get('cart')          #checking cart is empty or not before fetching anything
        if not cart:
            request.session.cart={}         
        ctg=Categories.get_category()
        prds=None
        category_ID = request.GET.get('Categories')
        if category_ID:
            prds=Product.get_products_category_id(category_ID)
        else:
            prds=Product.get_products
            context = {'category':ctg ,'product':prds }
            print('you are login as :',request.session.get('customer_email'))         #session have your given data ..going to use this soon
        return render (request,'home.html', context)
    else:    # handling post request 
        product_ids = request.POST.get('productid')
        print(product_ids)
        cart = request.session.get('cart', {})
        quantity = cart.get(product_ids, 0)
    
        cart[product_ids] = quantity + 1
    
        request.session['cart'] = cart
    
        print('updated cart', request.session['cart'])
        return redirect ('home')

def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()
    
    return render(request, 'search_results.html', {'products': products, 'query': query})    

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1  # Decrement quantity by 1
        else:
            del cart[str(product_id)]  # Remove the product if quantity becomes 0
        request.session['cart'] = cart
    return redirect('cart')  # Redirect to the cart page after removing an item

# Add an item to the cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = cart.get(str(product_id), 0)
    cart[str(product_id)] = quantity + 1
    request.session['cart'] = cart
    return redirect('cart')     

def pro (request):
    prds=None
    category_ID = request.GET.get('Categories')
    if category_ID:
        prds=Product.get_products_category_id(category_ID)
    else:
        prds=Product.get_products
    # prds=Product.get_products_category_id(category_id=3)    product from specific category id
    return render (request,'proby.html', {'product':prds})

def filtu (request, category_slug):
    category = Categories.objects.get(slug=category_slug)
    prds= Product.objects.filter(category=category)
    return render (request,'proby.html',{'category':category ,'product':prds })

def send_validation_email(request, customer_pk):
    try:
        customer = Customer.objects.get(pk=customer_pk)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid customer_pk.")

    # Get the current site
    current_site = get_current_site(request)

    # Construct the validation link
    validation_link = f"http://{current_site.domain}/validate/{customer_pk}/"

    # Render the email template
    email_subject = 'Email Verification'
    email_text = f"Please click the following link to verify your email: {validation_link}"
    email_message = render_to_string('email_verification.html', {
        'customer': customer,
        'validation_link': validation_link,
        'customer_pk': str(customer.pk),
    })

    # Send the email
    elmail = EmailMultiAlternatives(email_subject, email_text, 'test@gmail.com', [customer.email])
    elmail.attach_alternative(email_message, "text/html")
    elmail.send()
   
    return HttpResponse("Email verified !")

def verify_email(request, customer_pk):
    try:
        customer = Customer.objects.get(pk=customer_pk)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid customer_pk.")
    customer.is_verified = True
    customer.save()
    return render (request,'email_verified.html')

# Validation (E-mails, Passwords)
def validateCust(customer):
    global error_message 
    error_message = None
    if not customer.full_name:
        error_message = "Please enter your full name to proceed"
    elif len(customer.full_name) < 4:
        error_message = "Name must be more than 4 characters"
    elif not customer.email:
        error_message = "Email field can't be empty"   
    elif not customer.password:
        error_message = "Password field can't be empty"
    elif not customer.pass2:  # Check if pass2 field is not empty
        error_message = "Please enter the password again to confirm"
    elif customer.password != customer.pass2:  # Compare password and pass2 fields
        error_message = "Passwords do not match"
    elif not customer.email.endswith('@gmail.com'):
        error_message = "Only Gmail addresses are allowed"
    elif len(customer.password) < 8:
        error_message = "Password must be more than 8 characters"    
    elif not any(char.isalpha() for char in customer.password):
        error_message = "Password must contain at least one letter"
    elif not any(char.isupper() for char in customer.password):
        error_message = "Password must contain at least one uppercase letter"        
    elif not any(char.isdigit() for char in customer.password):
        error_message = "Password must contain at least one digit" 
    elif not any(char in '@$%&!_+' for char in customer.password):
        error_message = "Add one special character (can use @ $ % & ! _ +)"   
    elif customer.password.lower() == customer.email.split('@')[0].lower():
        error_message = "Password cannot be the same as Gmail address"            
    elif customer.isExists():
        error_message = "Email already exists."
    return error_message


def change_password(request):
    if request.method == "POST":
        postData = request.POST
        email = postData.get('email')
        old_password = postData.get('old_password')
        new_password = postData.get('new_password')
       

        customer = Customer.getCustByEmail(email)
       

     
       # print(old_password)
        #print(customer.password)
        
        if check_password(old_password, customer.password):
            
            hashed_new_password = make_password(new_password)
            customer.password = hashed_new_password
            customer.pass2 = hashed_new_password  # Update pass2 field if needed
            customer.save()
            return redirect('login')  # Redirect to login page after successful password change
           
        else:
            print(old_password)
            print(new_password)
            print(customer.password)
            error_message = "Incorrect old password."
        

        return render(request, 'change_password.html', {'error': error_message})
    else:
        return render(request, 'change_password.html')

 #Login Logic
def login (request,customer_pk=None):
   
    if request.method == "POST":

        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
       
        customer = Customer.getCustByEmail(email)
        
        if customer:                                                  # place : "and customer.is_verified :"
            flag = check_password(password, customer.password)
            if flag :
                request.session['customer_name']= customer.full_name              # requesting data to store in session
                request.session['customer_email']= customer.email
                
                return_url = request.GET.get('return_url') or request.session.get('return_url')
                
                if return_url:
                    # Redirect to the return_url if provided
                    return redirect(return_url)
                else:
                    # Redirect to the home page by default
                    return redirect('home')
                
            else:
                error_message = "Invalid Email or Password."
        else:
            error_message = "Invalid Email or Password."  
        return render (request,'login.html', {'error' : error_message})     
    else:
        return_url = request.GET.get('return_url')
        if return_url:
            request.session['return_url'] = return_url
        return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return redirect ('login')


# Signup Logic
def reg (request):

    if request.method == "POST":
        
        # username =  request.POST.get('fname')           
        # print(username)
        postData = request.POST
        full_name = postData.get('users')
        email = postData.get('email')
        password = postData.get('password')
        pass2 = postData.get('pass2')

       # print(full_name,email,password)

        revalue = {'full_name' : full_name , 'email' : email }         #values which we don't want to repeat in signup form
        error_message = None
        customer = Customer(full_name = full_name , email = email , password = password , pass2 = pass2)
        error_message = validateCust(customer)     #calling above method

    
        

        if (not error_message):   
        # Now creating customer object 
            customer.password = make_password(customer.password)
            customer.pass2 = make_password(customer.pass2)
            customer.save()
            #send_validation_email(request, customer.pk)                         #  uncomment this to get the email sending feature after registration
                    
            return redirect ('login')  
        else:                                                          #if error_message has some value
            data  = { 'revalue' : revalue , 'error' : error_message }     
            return render (request, 'register.html',data)              #printing them at the same register html page    
   
    else:
        return render (request,'register.html')
