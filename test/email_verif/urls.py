from django.urls import path
from . import views
from .views import Home

app_name = "email_verif"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register/", views.register_user, name="register"),
]
