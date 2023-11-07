from django import views
from django.urls import path, include
from . import views
from .views import Register_User
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

app_name = "profilemanager"

urlpatterns = [
    path("home", views.home, name="home"),
    path("", Register_User.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
