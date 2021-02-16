# Generated by Django 3.0.5 on 2021-02-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210215_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genre',
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genres', to='api.Genres'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
    ]