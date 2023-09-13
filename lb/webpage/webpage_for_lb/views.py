from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, "webpage_for_lb/home.html")
