from django.urls import path, include
from книги import views

app_name = "книги"

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.books, name="books"),
]
