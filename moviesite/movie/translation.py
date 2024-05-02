from .models import Movie
from modeltranslation.translator import TranslationOptions,register


@register(Movie)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category', 'marka', 'model', 'city', 'country', 'description')