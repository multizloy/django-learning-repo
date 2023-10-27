from .views import RegistrationView, UsernameValidationView, EmailValidationView

from django.urls import path
from django.views.decorators.csrf import csrf_exempt, csrf_protect

app_name = "authentication"

urlpatterns = [
    path("register/", csrf_exempt(RegistrationView.as_view()), name="register"),
    path(
        "validate-username/",
        csrf_exempt(UsernameValidationView.as_view()),
        name="validate-username",
    ),
    path(
        "validate-email/",
        csrf_exempt(EmailValidationView.as_view()),
        name="validate-email",
    ),
]
