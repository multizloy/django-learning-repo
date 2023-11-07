from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from profilemanager.forms import Register_User_Form

# Create your views here.


def home(request):
    return render(request, "main/home.html")


class Register_User(generic.CreateView):
    form_class = Register_User_Form

    template_name = "registration/register.html"
    success_url = reverse_lazy("profilemanager:login")
