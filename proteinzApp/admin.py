from django.contrib import admin
from proteinzApp.models import Product
from proteinzApp.models import Categories
from proteinzApp.models import Customer
from proteinzApp.models import Order

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category','markedprice']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']    
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Categories,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
