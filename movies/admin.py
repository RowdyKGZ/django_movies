from django import forms
from django.contrib import admin

from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Actor, Genre, Movie, MovieShot, Rating, RatingStar, Review


class MovieAdminForm(forms.ModelForm):
    """Подключение CKeditor для описания"""
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Катеогрий в админке"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):
    """Добавляем к фильмям отзывы в админке"""
    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    """Инлайг для фоток фильма"""
    model = MovieShot
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Подключаем фильмы и отзывы к фильмам"""
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInLine]
    form = MovieAdminForm
    actions = ['publish', 'unpublish']
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', 'poster', 'get_image', ('year', 'world_premier'), 'country')
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

    def get_image(self, obj):
        """Отображение каринок в админке"""
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = 'Изображение'

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликавать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permission = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permission = ('change',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(Actor)
class ReviewAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Genre)
class ReviewGenre(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name',)


@admin.register(MovieShot)
class ReviewMovieShot(admin.ModelAdmin):
    """Кадры к фильмам"""
    list_display = ('title', 'movie', 'get_image')

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(RatingStar)
class ReviewRating(admin.ModelAdmin):
    """Звезды рейтинга"""
    list_display = ('value',)


@admin.register(Rating)
class ReviewRating(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('star', 'movie')


admin.site.site_title = 'Django Rowdy Movies'
admin.site.site_header = 'Django Rowdy Movies'
