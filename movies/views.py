from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie, Category, Actor, Genre
from .forms import ReviewForm


class GenreYear:
    """Жанры и годы выходов фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MovieView(GenreYear, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movie_list.html'


class MovieDetailView(GenreYear, DetailView):
    """Детали фильма"""
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзыв"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    """Вывод информации об актере"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):
    """Фильтрация фильмов"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset
