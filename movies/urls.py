from django.urls import path

from .views import MovieView, MovieDetail, AddReview

urlpatterns = [
    path('', MovieView.as_view(), name='movies'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
]
