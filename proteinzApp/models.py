import datetime
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    pass2 = models.CharField(max_length=500 , null = True)
    is_verified = models.BooleanField(default=False)

    @staticmethod
    def getCustByEmail(email):
        try:
            return Customer.objects.get(email=email)      #matching Login current email with email in django admin
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):      #matching Signup current email with email in django admin
            return True
        else:
            return False

class Order(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50,default='',blank=True)  # Add this field
    product_name = models.CharField(max_length=50,default='',blank=True)   # Add this field
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)
    
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    markedprice=models.IntegerField(default=0)
    category = models.ForeignKey('Categories',on_delete=models.CASCADE ,default=1)
    description = models.CharField(max_length=190,default='')
    Image = models.ImageField(upload_to='uploads/products')
    Image2 = models.ImageField(upload_to='uploads/products',default="")

    @staticmethod
    def get_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_ids(product_ids):
        return Product.objects.filter(id__in=product_ids)
    
    @staticmethod
    def get_products_category_id(category_id):
        return Product.objects.filter(category=category_id)

class Categories(models.Model):
    name=models.CharField(max_length=50)
    description = models.CharField(max_length=190,default='')
    Image = models.ImageField(upload_to='uploads/category')  
    slug = models.SlugField(null=True,blank=True)
    
    @staticmethod
    def get_category():
        return Categories.objects.all()
    
    def  __str__(self):
        return self.name
    
    def save (self, *args, **kwargs):                # to get the same name of slugs as category 
        self.slug = slugify(self.name)
        super(Categories,self).save (*args, **kwargs)
