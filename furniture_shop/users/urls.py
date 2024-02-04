from django.urls import path

from . import views
from users.views import *

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("users-cart/", users_cart, name="users_cart"),
]
