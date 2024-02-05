from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories
# Create your views here.


def index(request):
    
    context = {
        "title": "Main Page",
        "content": "This is the main page.",
        
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About page",
        "content": "This is the about page.",
    }
    return render(request, "main/about.html", context)

