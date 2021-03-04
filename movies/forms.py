from django import forms

from .models import Review, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Review
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    """Форма райтинга фильма"""
    star = forms.ModelChoiceField(
        queryset= RatingStar.objects.all(), widget=forms.RadioSelect, empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
