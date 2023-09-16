from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(
        request, "core/index.html", {"title": "Главная страница сайта", "tasks": tasks}
    )


def about(request):
    return render(
        request,
        "core/about.html",
        {
            "title": "О нас",
        },
    )


def create(request):
    error = ""
    if request == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("index")
        else:
            error = "Форма была неверной"
    form = TaskForm()
    context = {"form": form, "error": error}
    return render(request, "core/create.html", {"title": "Создать"})
