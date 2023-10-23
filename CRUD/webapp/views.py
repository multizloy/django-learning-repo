from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "webapp/home.html")


# Register
def register(request):
    form = CreateUserForm()

    context = {"form": form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("webapp:login")
    return render(request, "webapp/register.html", context)


# login an user
def my_login(request):
    form = LoginForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in!")
                return redirect("webapp:dashboard")

    return render(request, "webapp/my-login.html", context)


# user logout
def logout(request):
    auth.logout(request)
    return redirect("webapp:login")


# Dashboard
@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {"records": my_records}
    return render(request, "webapp/dashboard.html", context)


# Create a record
@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully!")
            return redirect("webapp:dashboard")

    context = {
        "form": form,
    }
    return render(request, "webapp/create-record.html", context)


# update a record
@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully!")
            return redirect("webapp:dashboard")

    context = {"form": form}
    return render(request, "webapp/update-record.html", context)


# Read/View a singular record
@login_required(login_url="login")
def view_record(request, pk):
    all_record = Record.objects.get(id=pk)
    context = {"records": all_record}
    return render(request, "webapp/view-record.html", context)


# delete record
@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Account deleted successfully!")
    return redirect("webapp:dashboard")
