from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Titles(models.Model):
    name = models.CharField(
        "Название произведения", max_length=100,
        blank=True,
        null=True
        )
    year = models.IntegerField("Год выпуска")
    description = models.TextField("Описание")
    genre =  models.ManyToManyField(
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

