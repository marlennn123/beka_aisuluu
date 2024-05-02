from rest_framework import viewsets, permissions
from .serializers import *
from .models import *


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ActorViewSets(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieShotsViewSets(viewsets.ModelViewSet):
    queryset = MovieShots.objects.all()
    serializer_class = MovieShotsSerializers


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers


class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers