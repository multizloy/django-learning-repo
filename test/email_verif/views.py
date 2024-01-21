from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django_email_verification import send_email


from django.views import generic

# Create your views here.


class Home(generic.TemplateView):
    template_name = "email_verif/home.html"


def register_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data["email"]
            user_username = form.cleaned_data["username"]
            user_password = form.cleaned_data["password1"]

            # Create new user
            user = User.objects.create_user(
                username=user_username, email=user_email, password=user_password
            )

            # Make user unactive until they click link to token in email
            user.is_active = False
            send_email(user)

            return HttpResponseRedirect(reverse("email_verif:home"))

    return render(request, "email_verif/register.html", {"form": form})
