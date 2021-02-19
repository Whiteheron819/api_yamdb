from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.TextField(
        "Название категории",
        blank=True,
        null=True)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        blank=True,
        null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(
        "Название жанра",
        blank=True,
        null=True)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        blank=True,
        null=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        "Название произведения", max_length=100,
        blank=True,
        null=True)
    year = models.IntegerField("Год выпуска")
    description = models.TextField("Описание")
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="titles",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField('Отзыв')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.IntegerField('Оценка')


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
