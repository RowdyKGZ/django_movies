from django.urls import path

from .views import MovieView, MovieDetail

urlpatterns = [
    path('', MovieView.as_view(), name='movies'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
]
