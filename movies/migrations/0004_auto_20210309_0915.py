# Generated by Django 3.0.3 on 2021-03-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210307_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='actor',
            name='name_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорий'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорий'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movieshot',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshot',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='movieshot',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='movieshot',
            name='title_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
    ]