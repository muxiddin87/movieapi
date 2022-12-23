from rest_framework import serializers
from datetime import date


from .models import Movie, Actor, Comment
from rest_framework.exceptions import ValidationError


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, birthdate):
        if birthdate < date.fromisoformat('1950-01-01'):
            raise ValidationError('1950-01-01 dan kattaroq sana yozing')
        return birthdate



class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actors')


class CommentSerializer(serializers.ModelSerializer):
    movie_id = MovieSerializer
    class Meta:
        model = Comment
        fields = ("id", "movie_id", "user_id", "text", "created_date")









