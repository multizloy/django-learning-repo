from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "expenses/home.html")


def add_expenses(request):
    return render(request, "expenses/add-expenses.html")
