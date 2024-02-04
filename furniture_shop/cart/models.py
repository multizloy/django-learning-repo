from django.db import models


# Create your models here.
class Cart_Queryset(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        "goods.Products", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=50, blank=True, null=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("-created_timestamp",)

    objects = Cart_Queryset.as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт: {self.product.name} | Количество: {self.quantity}"
