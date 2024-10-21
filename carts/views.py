from django.shortcuts import get_object_or_404, redirect, render
from carts.models import Cart
from goods.models import Products

def cart_add(request,product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product = product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity +=1
                cart.save()
        else:
            Cart.objects.create(user = request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    cart = get_object_or_404(Cart, user=request.user, product=product)
    cart.quantity += 1
    cart.save()
    return redirect(request.META['HTTP_REFERER'])

def cart_dicrement(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    cart = get_object_or_404(Cart, user=request.user, product=product)
    cart.quantity -= 1 
    if cart.quantity < 1:
        cart.delete()
        return redirect(request.META['HTTP_REFERER'])
    cart.save()
    return redirect(request.META['HTTP_REFERER'])
    

def cart_remove (request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])