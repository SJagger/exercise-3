from django.db import models

# Create your models here.

class BookList(models.Model):
    """docstring for BookList."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.IntegerField()
    price = models.IntegerField()

class MovieList(models.Model):
    """docstring for MovieList."""
    mtitle = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    rating = models.FloatField()

class TvShowList(models.Model):
    """docstring for TvShowList."""
    ttitle = models.CharField(max_length=200)
    seasons = models.IntegerField()
    network = models.CharField(max_length=150)
    episodes = models.IntegerField()
