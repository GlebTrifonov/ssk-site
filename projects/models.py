from django.db import models
from PIL import Image

from services.models import Service


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        verbose_name="Услуга",
        related_name="projects",
    )
    is_active = models.BooleanField(default=True, verbose_name="Показывать на сайте")

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=200, verbose_name="Имя")
    text = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Показывать на сайте")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("-created_at",)

    def __str__(self):
        return self.author


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Объект", related_name="images"
    )
    image = models.ImageField(upload_to="project/", verbose_name="Фото")

    class Meta:
        verbose_name = "Фото объекта"
        verbose_name_plural = "Фото объектов"

    def __str__(self):
        return f"{self.project}, фото {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.thumbnail((1600, 1600))
        img.save(self.image.path)
