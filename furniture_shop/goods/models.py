from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Ссылка"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Ссылка"
    )
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, null=True, verbose_name="Фото"
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f'{self.name} Количество: {self.quantity}'
