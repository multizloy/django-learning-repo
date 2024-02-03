from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from .forms import User_Login_Form


# Create your views here.
def login(request):
    if request.method == "POST":
        form = User_Login_Form(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                # return render(request, "users/profile.html")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = User_Login_Form()

    context = {
        "title": "Login page",
        "form": form,
    }
    return render(request, "users/login.html", context)


def register(request):
    context = {
        "title": "Register page",
    }
    return render(request, "users/register.html", context)


def profile(request):
    context = {
        "title": "Profile page",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    context = {
        "title": "Logout page",
    }
    return render(request, "users/logout.html", context)
