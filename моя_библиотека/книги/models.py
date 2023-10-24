from django.db import models
from django.urls import reverse

# Create your models here.


# модель для выбора жанра книги
class Жанр(models.Model):
    Название = models.CharField(
        max_length=50,
        help_text="Напишите название жанра(Например: Фантастика, Триллер, Приключения и т.д.)",
    )

    def __str__(self):
        return self.Название


# создаем модель языка книги
class Язык(models.Model):
    язык = models.CharField(
        max_length=50,
        help_text="Введите язык, на котором написана книга(например: Английский, Французский, Русский и т.д.)",
    )

    def __str__(self):
        return self.язык


class Автор(models.Model):
    имя = models.CharField(max_length=50, help_text="Введите имя автора")
    фамилия = models.CharField(max_length=50, help_text="Введите фамилию автора")

    def __str__(self):
        return self.имя + "  " + self.фамилия


# cоздаем модель описания книг
class Книги(models.Model):
    название = models.CharField(max_length=50)
    описание = models.TextField(help_text="Краткое описание книги")
    жанр = models.ManyToManyField(Жанр, help_text="Выберите жанр для этой книги")
    автор = models.ForeignKey("Автор", on_delete=models.SET_NULL, null=True)
    язык_книги = models.ForeignKey("Язык", on_delete=models.SET_NULL, null=True)
    год_издания = models.IntegerField()

    def display_genre(self):
        """Создаем строку для жанров. Обязательно для вывода жанров в админ панели."""
        return ", ".join([жанр.название for жанр in self.жанр.all()[:3]])

    def __str__(self):
        return self.название
