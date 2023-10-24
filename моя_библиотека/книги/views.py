from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "книги/home.html")


def books(request):
    return render(request, "книги/books.html")
