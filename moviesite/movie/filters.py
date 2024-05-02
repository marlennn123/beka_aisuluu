from django_filters.rest_framework import FilterSet
from .models import *


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'category': ['exact'],
            'title': ['gt', 'lt']
        }