from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path("employee/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create/createData/", views.createData, name="create-data"),
    path("update/updateData/<int:id>", views.updateData, name="update-data"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("", views.blog, name="blog"),
    path("details/<int:id>", views.detailsPage, name="details"),
]
