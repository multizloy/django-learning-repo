from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Record

# register/create an user


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        verbose_name = "CreateUserName"
        verbose_name_plural = "CreateUserNames"


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name", "last_name", "email", "phone", "country"]


# update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name", "last_name", "email", "phone", "country"]
