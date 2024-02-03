from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from .forms import User_Login_Form, User_Registration_Form


# Create your views here.
def login(request):
    # if user.is_authenticated:
    #     return HttpResponseRedirect(reverse("main:index"))
    
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
    if request.method == "POST":
        form = User_Registration_Form(data=request.POST)
        if form.is_valid():
            form.save()

            # session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            # if session_key:
            #     Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(
                request,
                f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = User_Registration_Form()

    context = {"title": "Home - Регистрация", "form": form}
    return render(request, "users/register.html", context)


def profile(request):
    context = {
        "title": "Profile page",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("users:login"))
