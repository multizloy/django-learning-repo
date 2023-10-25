from .views import RegistrationView

from django.urls import path

app_name = "authentication"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
]
