from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        "title": "Main Page",
        "content": "This is the main page.",
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("Hello, world. You're at the shop about.")
