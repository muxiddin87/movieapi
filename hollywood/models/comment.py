from django.contrib.auth import get_user_model
from django.db import models
from .movie import Movie

User = get_user_model()

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
