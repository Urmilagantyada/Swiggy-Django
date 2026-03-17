from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/<int:id>/", views.menu, name="menu"),
    path("cart/", views.cart_view, name="cart"),
    path("add-to-cart/<int:food_id>/", views.add_to_cart, name="add_to_cart"),
    path("increase/<int:food_id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:food_id>/", views.decrease_quantity, name="decrease_quantity"),
    path("remove/<int:food_id>/", views.remove_from_cart, name="remove_from_cart"),
]