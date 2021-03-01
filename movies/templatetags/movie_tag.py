from django import template
from movies.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """тэг для категорий в хидерс"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count):
    """тэг для последних фильмов в сайдбаре"""
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': movies}
