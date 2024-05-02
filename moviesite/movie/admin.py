from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Reviews)


@admin.register(Movie)
class ProductAdmin(TranslationAdmin):
    list_display = ("title",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }