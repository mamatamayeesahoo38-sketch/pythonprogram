from django.shortcuts import render, redirect

# Simple product list (no database)
products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Headphone", "price": 2000},
}

# 1️⃣ Home Page
def home(request):
    return render(request, "cartapp/home.html", {"products": products})

# 2️⃣ Add to Cart
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    
    request.session['cart'] = cart
    return redirect('cart')

# 3️⃣ View Cart
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for id, quantity in cart.items():
        product = products[int(id)]
        subtotal = product["price"] * quantity
        total += subtotal
        cart_items.append({
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "subtotal": subtotal
        })

    return render(request, "cartapp/cart.html", {
        "cart_items": cart_items,
        "total": total
    })

# 4️⃣ Checkout
def checkout(request):
    request.session['cart'] = {}
    return render(request, "cartapp/checkout.html")
