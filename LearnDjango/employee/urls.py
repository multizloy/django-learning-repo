from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create/createData/", views.createData, name="create-data"),
]
