from django.db import models


class Titles(models.Model):
    name = models.CharField(
        "Название произведения", max_length=100,
        blank=True,
        null=True
        )
    year = models.IntegerField("Год выпуска")
    description = models.TextField("Описание")
    genre = models.ManyToManyField(
        'Genres',
        related_name="genres",
        blank=True,
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        related_name="categories",
        blank=True,
        null=True,
    )
