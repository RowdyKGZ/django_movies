from django.contrib import admin

from .models import Category, Actor, Genre, Movie, MovieShot, Rating, RatingStar, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', 'poster', ('year', 'world_premier'), 'country')
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('directors', 'actors'),)
        }),
        (None, {
            'fields': ('genres', 'category', 'draft', 'url')
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(Actor)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Genre)
class ReviewGenre(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MovieShot)
class ReviewMovieShot(admin.ModelAdmin):
    list_display = ('title', 'movie')


@admin.register(RatingStar)
class ReviewRating(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class ReviewRating(admin.ModelAdmin):
    list_display = ('star', 'movie')




