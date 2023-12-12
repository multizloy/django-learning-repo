from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name
    
class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    
    class Meta:
        ordering = ["name"]
        unique_together = ("category", "name", )
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self) -> str:
        s = self.name
        if not self.in_stock:
            s = s + "(нет в наличии)"
        return s
    