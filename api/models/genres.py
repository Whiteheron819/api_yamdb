from django.db import models


class Genres(models.Model):
    name = models.TextField(
        "Название жанра",
        blank=True,
        null=True)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        blank=True,
        null=True)
