# Ecom_proteinz

**Developed by:** [Manu Prasad](https://github.com/manu09)

## Proteinz is an e-commerce like website where users can : 

<h3>SIGNUP :</h3>

![signup](https://github.com/manuo9/Ecom_proteinz/assets/122933806/92b80af9-257c-4ab3-854b-9d79cbc018cf)
<hr>
<h3>LOGIN WITH EMAIL AUTHENTICATION :</h3>

![login](https://github.com/manuo9/Ecom_proteinz/assets/122933806/9bfa5bdb-2c01-4854-98d3-edf7236b2413)

![gmail](https://github.com/manuo9/Ecom_proteinz/assets/122933806/52a09e8b-755b-4f0b-b61f-240a971b3a42)

![suceslogin](https://github.com/manuo9/Ecom_proteinz/assets/122933806/e0364992-0260-43d0-9b62-60a2e01a9394)

<h3>To use the email authentication feature :</h3> 

• uncomment  #send_validation_email(request, customer.pk) line 332 in views.py

• write "and customer.is_verified :" with if condition in line 273  in views.py

• In settins.py file, You have to give your email and password
  
<pre>• EMAIL_HOST_USER = 'youremail@gmail.com'
• EMAIL_HOST_PASSWORD = 'your email password'
</pre>
• Login to gmail through host email id in your browser and open following link and turn it ON

<pre>https://myaccount.google.com/lesssecureapps</pre>

<hr>
<h3>VIEW CATEGORY/PRODUCT :</h3>

![product](https://github.com/manuo9/Ecom_proteinz/assets/122933806/045f1f99-55fa-4c8c-837a-795a57375840)

![cate](https://github.com/manuo9/Ecom_proteinz/assets/122933806/81f6b9b8-aee3-4e34-9999-a4b1acc4045b)
<hr>
<h3>SEARCH PRODUCT :</h3>

![Screenshot (97)](https://github.com/manuo9/Ecom_proteinz/assets/122933806/33473b24-2631-43ae-bea3-5d9ebf71f167)
<hr>
<h3>INFO PAGE WITH FEW IMAGES :</h3>

![Screenshot (98)](https://github.com/manuo9/Ecom_proteinz/assets/122933806/1be2ed59-1206-4623-b07a-1da60486edb0)
<hr>
<h3>CHANGE PASSWORD :</h3>

![forgot](https://github.com/manuo9/Ecom_proteinz/assets/122933806/d6cb1fb7-d323-420f-9081-c8eddfa04bbb)
<hr>
<h3>VIEW CART / ADD OR REMOVE PRODUCTS :</h3>

![cart](https://github.com/manuo9/Ecom_proteinz/assets/122933806/0e5f9d94-c625-413b-a8da-1c06e522345f)
<hr>
<h3>CHECKOUT WITH ADDRESS & PHONE NUMBER : </h3>

![checkout](https://github.com/manuo9/Ecom_proteinz/assets/122933806/5d417c37-0c0c-4792-8c04-434c76ba8e43)
<hr>
<h3>VIEW YOUR ORDERS AFTER CHECKOUT WITH STATUS (DONE BY ADMIN) :</h3>

![orders](https://github.com/manuo9/Ecom_proteinz/assets/122933806/961e5512-3c65-4b80-b959-a23fb6189b7a)
<hr>
<h3>Extras :  (chatbot) </h3> 

![chatbot](https://github.com/manuo9/Ecom_proteinz/assets/122933806/bbdf58ff-1abc-44cd-8fe2-7c82c0a6b753)

<h4>• Chatbot was made with Google Dialogflow , intents were made there , then i integrated with Kommunicate which gives you good visuals/ui and control over agent and conversation.</h4>
<pre>https://www.kommunicate.io </pre>
<h4>• Kommunicate will give you script , pasting it in our code will give us the chatbot at one side of the website, through which we can interact and get all necessary information.</h4>

<h4>• <i>Script is still in the code, but won't work now as kommunicate is not free ,it was a free trial and i am not paying for it.</i>i></h4>

<hr>
<h2>Installation</h2>

<h3># Clone this repository to your local machine: </h3>

<pre>git clone https://github.com/manuo9/Ecom_proteinz.git</pre>

<h3># Install the required dependencies:</h3>

<pre>pip install -r requirements.txt</pre> 

 <h3># Set up your Django project:</h3>

• Create a virtual environment (recommended) and activate it.

• Configure your database settings in settings.py.

• Apply migrations using <code>python manage.py migrate</code>.

• Create a superuser account with <code>python manage.py createsuperuser</code>.

• Launch the development server: <code>python manage.py runserver </code>

• Access the application in your web browser at <code>http://localhost:8000/</code>

<hr>
 <h3># Contributing </h3>
 <h4> We welcome contributions to Proteinz! Whether it's bug fixes, new features, or improvements to the documentation, your contributions help make this project better for everyone.</h4>
<hr>
<h3>Disclaimer</h3>
<h4> This project is developed for demo purpose and it's not supposed to be used in real application. </h4>















