from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Sign_Up_Form


# Create your views here.
def home(request):
    # check to see if logging in (проверка вошел ли юзер в аккаунт)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # удостоверение (authenticate)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home.html")
        else:
            messages.success(
                request, "There was an error logging in, please try again..."
            )
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "YOu have successfully log in")
            return redirect("home")
    else:
        form = Sign_Up_Form()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})
