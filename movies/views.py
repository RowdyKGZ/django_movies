from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie


class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'
    

class MovieDetail(DetailView):
    """Детали фильма"""
    model = Movie
    slug_field = 'url'
