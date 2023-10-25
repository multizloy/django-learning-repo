from django.urls import path
from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.home, name="expenses"),
    path("add-expenses", views.add_expenses, name="add-expenses"),
]
