from django.shortcuts import render
from django.views import View

from .models import Movie


class MovieView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})
