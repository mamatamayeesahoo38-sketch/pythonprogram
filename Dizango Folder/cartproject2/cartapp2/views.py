from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    products = Product.objects.all()
    return render(request, "cartapp2/home.html", {"products": products})


# Add to cart
@login_required
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


# View cart
@login_required
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, id=id)
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

    return render(request, "cartapp2/cart.html", {
        "cart_items": cart_items,
        "total": total
    })


# Remove item
@login_required
def remove_item(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')


# Update quantity
@login_required
def update_quantity(request, id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    cart[str(id)] = quantity
    request.session['cart'] = cart
    return redirect('cart')


# Checkout
@login_required
def checkout(request):
    request.session['cart'] = {}
    return render(request, "cartapp2/checkout.html")
