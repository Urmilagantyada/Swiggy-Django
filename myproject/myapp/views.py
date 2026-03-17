from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Food


def home(request):
    query = request.GET.get("q", "")
    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)
    else:
        restaurants = Restaurant.objects.all()

    return render(request, "index.html", {
        "restaurants": restaurants,
        "query": query
    })


def menu(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    foods = Food.objects.filter(restaurant=restaurant)

    return render(request, "menu.html", {
        "restaurant": restaurant,
        "foods": foods
    })


def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    cart = request.session.get("cart", {})

    food_id_str = str(food_id)
    if food_id_str in cart:
        cart[food_id_str]["quantity"] += 1
    else:
        cart[food_id_str] = {
            "name": food.name,
            "price": food.price,
            "quantity": 1,
            "image": food.image if food.image else ""
        }

    request.session["cart"] = cart
    return redirect("cart")


def cart_view(request):
    cart = request.session.get("cart", {})
    total = 0

    for item in cart.values():
        item["subtotal"] = item["price"] * item["quantity"]
        total += item["subtotal"]

    return render(request, "cart.html", {
        "cart": cart,
        "total": total
    })


def increase_quantity(request, food_id):
    cart = request.session.get("cart", {})
    food_id_str = str(food_id)

    if food_id_str in cart:
        cart[food_id_str]["quantity"] += 1

    request.session["cart"] = cart
    return redirect("cart")


def decrease_quantity(request, food_id):
    cart = request.session.get("cart", {})
    food_id_str = str(food_id)

    if food_id_str in cart:
        cart[food_id_str]["quantity"] -= 1
        if cart[food_id_str]["quantity"] <= 0:
            del cart[food_id_str]

    request.session["cart"] = cart
    return redirect("cart")


def remove_from_cart(request, food_id):
    cart = request.session.get("cart", {})
    food_id_str = str(food_id)

    if food_id_str in cart:
        del cart[food_id_str]

    request.session["cart"] = cart
    return redirect("cart")