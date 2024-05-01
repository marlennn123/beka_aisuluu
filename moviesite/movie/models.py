from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='actor/')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='director/')


class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    plot = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name