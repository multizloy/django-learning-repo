from django.shortcuts import render


# Create your views here.
def login(request):
    context = {
        "title": "Login page",
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

