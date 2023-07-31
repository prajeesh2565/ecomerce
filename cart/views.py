from django.shortcuts import get_object_or_404, render,redirect
from shop.models import product
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,p_id):
    products=product.objects.get(id=p_id)
    try:
        Cart=cart.objects.get(cart_id=cart_id(request))
    except cart.DoesNotExist:
        Cart=cart.objects.create(cart_id=cart_id(request))
        Cart.save(),
    try:
        cart_item=cart_items.objects.get(product=products,cart=Cart)
        if cart_item.quantity < cart_item.product.stock :
            cart_item.quantity +=1
        cart_item.save()
    except cart_items.DoesNotExist:
        cart_item=cart_items.objects.create(product=products,quantity=1,cart=Cart)
        cart_item.save()
    return redirect('cart:cart_details')

def cart_details(request,total=0,counter=0,cart_item=None):
    try:
        Cart=cart.objects.get(cart_id=cart_id(request))
        cart_item=cart_items.objects.filter(cart=Cart,active=True)
        for obj in cart_item:
            total +=obj.product.price * obj.quantity
            counter +=obj.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_item=cart_item,total=total,counter=counter))

def cart_remove(request,product_id):
    Cart=cart.objects.get(cart_id=cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=cart_items.objects.get(product=products,cart=Cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_details')

def cart_delete(request,product_id):
    Cart=cart.objects.get(cart_id=cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=cart_items.objects.get(cart=Cart,product=products)
    cart_item.delete()
    return redirect('cart:cart_details')
