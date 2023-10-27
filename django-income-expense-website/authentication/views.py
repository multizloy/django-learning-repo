from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.contrib import messages

# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]

        if not str(username).isalnum():
            return JsonResponse(
                {
                    "username_error": "username should only contain alphanumeric characters"
                },
            )
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                ({"username_error": "This username taken, choice another username"}),
            )
        return JsonResponse({"username_valid": True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]

        if not str(email).isalnum():
            return JsonResponse(
                {"email_error": "Email taken"},
            )
        if User.objects.filter(email=email).exists():
            return JsonResponse(
                ({"username_error": "This username taken, choice another username"}),
            )
        return JsonResponse({"username_valid": True})


class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        # get user data , validate , create an user acc
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "password is to low")
                    return render(request, "authentication/register.html")
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.error(request, "Account successfully created")
                return render(request, "authentication/register.html")

        return render(request, "authentication/register.html")
