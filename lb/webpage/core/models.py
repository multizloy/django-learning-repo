from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    photo_img = models.ImageField("Фотография")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
