from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from users.models import User


class User_Login_Form(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль")

    # username = forms.CharField(
    #     label="Имя",
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     ),
    # )
    # password = forms.CharField(
    #     label="Пароль",
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",
    #             "placeholder": "Введите ваш пароль",
    #         }
    #     ),
    # )

    class Meta:
        model = User
        fields = ("username", "password")


class User_Registration_Form(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class Profile_Form(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
