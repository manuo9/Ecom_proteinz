from django.contrib import admin
from django.urls import path
from proteinzApp import views


urlpatterns = [
    path('',views.inde),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('home',views.inde,name='home'),
    path('search/', views.search_products, name='search_products'),
    path('products',views.pro,name='product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('login',views.login,name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout',views.logout,name='logout'),
    path('register',views.reg,name='regi'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.orders,name='orders'),
    path('validate/<int:customer_pk>/', views.verify_email, name='verify_email'),
    path('probycat/<slug:category_slug>',views.filtu,name='probycat'),
]