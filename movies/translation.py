from modeltranslation.translator import register, TranslationOptions

from .models import Category, Actor, Movie, Genre, MovieShot


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOption(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(MovieShot)
class MovieShotTranslationOption(TranslationOptions):
    fields = ('title', 'description')
