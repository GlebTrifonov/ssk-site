from django.core.validators import RegexValidator
from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя посетителя")
    phone = models.CharField(
        max_length=13,
        verbose_name="Телефон",
        validators=[
            RegexValidator(
                regex=r"^[+]375\d{9}$", message="Введите номер в формате +375XXXXXXXXX"
            )
        ],
    )
    message = models.TextField(blank=True, verbose_name="Что нужно сделать")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
