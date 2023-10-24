from django.contrib import admin
from .models import Автор, Жанр, Книги, Язык

# Register your models here.

admin.site.register(Автор)
admin.site.register(Жанр)
admin.site.register(Книги)
admin.site.register(Язык)
