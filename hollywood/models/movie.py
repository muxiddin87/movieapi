from django.db import models
from .actor import Actor


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=True)
    imdb = models.FloatField(default=True)
    genre = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name

