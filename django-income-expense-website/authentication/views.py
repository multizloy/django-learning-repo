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
        messages.success(request, "Success")
        return render(request, "authentication/register.html")
