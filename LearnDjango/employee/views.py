from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employee, BlogPosts
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
    return redirect(reverse("employee:index"))


def delete(request, id):
    delete_employee = Employee.objects.get(id=id)
    delete_employee.delete()
    return redirect(reverse("employee:index"))


def update(request, id):
    update_Employee = Employee.objects.get(id=id)
    context = {"Employee": update_Employee}
    return render(request, "employee/updatePage.html", context)


def updateData(request, id):
    name = request.POST["name"]
    title = request.POST["title"]
    update_Employee = Employee.objects.get(id=id)
    update_Employee.name = name
    update_Employee.title = title
    update_Employee.save()

    return redirect(reverse("employee:index"))


def blog(request):
    posts = BlogPosts.objects.all()
    featuredPost = BlogPosts.objects.filter(featured=True)
    context = {
        "posts": posts,
        "featuredPost": featuredPost,
    }
    return render(request, "employee/blog.html", context)


def detailsPage(request, id):
    detailsPost = BlogPosts.objects.get(id=id)
    template = loader.get_template("employee/detailsPage.html")
    context = {"posts": detailsPost}
    return HttpResponse(template.render(context, request))
