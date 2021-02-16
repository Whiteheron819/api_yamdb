from django.db import models


class Categories(models.Model):
    name = models.TextField(
        "Название категории",
        blank=True,
        null=True)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        blank=True,
        null=True)
