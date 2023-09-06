from django import template

from proteinzApp.models import Product

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return ("Added")
   # print(product)
    return ("Yet to add")

@register.filter(name='get_product')
def get_product(product_id):
    return Product.objects.get(id=product_id)

@register.filter(name='calculate_total')
def calculate_total(price, quantity):
    return price * quantity

@register.filter(name='all_total')
def all_total(cart):
    total = 0
    if isinstance(cart, dict):
        for product_id, quantity in cart.items():
            prds = get_product(product_id)
            total += calculate_total(prds.price, quantity)
    return total


