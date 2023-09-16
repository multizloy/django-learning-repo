from django import forms

from .models import Photo

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = (
            "name",
            "description",
            "photo_image",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "photo_image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
