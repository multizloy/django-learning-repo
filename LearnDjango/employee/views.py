from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from django.urls import reverse

# Create your views here.


def index(request):
    myEmployees = Employee.objects.all().values()
    context = {
        "myEmployees": myEmployees,
    }
    return render(request, "employee/index.html", context)


def create(request):
    return render(request, "employee/createPage.html")


def createData(request):
    data_1 = request.POST["name"]
    data_2 = request.POST["title"]
    new_Employee = Employee(name=data_1, title=data_2)
    new_Employee.save()
    return redirect(reverse("employees:index"))
