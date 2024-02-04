from django.urls import path

from cart.views import *

app_name = "cart"

urlpatterns = [
    path("cart_add/<int:product_id>/", cart_add, name="cart_add"),
    path("cart_remove/<int:product_id>/", cart_remove, name="cart_remove"),
    path("cart_change/<int:product_id>/", cart_change, name="cart_change"),
]
