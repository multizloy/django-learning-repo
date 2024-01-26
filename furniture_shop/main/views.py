from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories
# Create your views here.


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Main Page",
        "content": "This is the main page.",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About page",
        "content": "This is the about page.",
    }
    return render(request, "main/about.html", context)
