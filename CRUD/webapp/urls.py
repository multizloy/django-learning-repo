from django.urls import path, include
from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.home, name="home"),
]
