from django.db import models


# Create your models here.
class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "      " + self.last_name
