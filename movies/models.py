from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категорий"""
    name = models.CharField('Категорий', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Катоегрия'
        verbose_name_plural = "Категорий"


class Actor(models.Model):
    name = models.CharField('Имя', max_length=150)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и Режиссеры'
        verbose_name_plural = "Актеры и Режиссеры"


class Genre(models.Model):
    name = models.CharField('Имя', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильмы"""
    title = models.CharField('Название', max_length=150)
    tagline = models.CharField('Слоган', max_length=150)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2021)
    country = models.CharField('Страна', max_length=150)
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premier = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveSmallIntegerField('Бюджет', default=0, help_text='Указывать сумму в долларах')
    fees_in_usa = models.PositiveSmallIntegerField('Сбры в США', default=0, help_text='Указывать сумму в долларах')
    fees_in_world = models.PositiveSmallIntegerField('Сборы в мире', default=0, help_text='Указывать сумму в долларах')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = "Фильмы"

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})


class MovieShot(models.Model):
    """Кадры к фильму"""
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр к фильму'
        verbose_name_plural = "Кадры к фильму"


class RatingStar(models.Model):
    """Звезды рейтнг"""
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинг'
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Отзыв', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв к фильму'
        verbose_name_plural = "Отзывы к фильму"

