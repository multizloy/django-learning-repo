from django.db import models

# Create your models here.
class Horoscope(models.Model):
    name = models.CharField(max_length=200)
    context = models.TextField()
    
    def __str__(self):
        return self.name