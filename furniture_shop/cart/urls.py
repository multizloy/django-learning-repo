from django.urls import path

from cart.views import *

app_name = "cart"

urlpatterns = [
    path("cart_add/<slug:product_slug>/", cart_add, name="cart_add"),
    path("cart_remove/<int:cart_id>/", cart_remove, name="cart_remove"),
    path("cart_change/<slug:product_slug>/", cart_change, name="cart_change"),
]
