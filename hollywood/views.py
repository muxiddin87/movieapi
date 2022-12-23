import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor, Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

class HelloWorldAPIView(APIView):
    def get(self,request):
        return Response(data={"message": "Hello World"})

class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        data = request.data
        serializer = ActorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data)


    def delete(self, request):
        data = request.data
        serializer = ActorSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.delete()
        return Response({'status': 200, 'message': "o'chirildi"})

class MovieActorAPIView(APIView):
    def get(self, request):
        pass

"""User = get_user_model()
class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)



class CommentAPIView(APIView):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        def get(self, request):
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(data=serializer.data)

        def post(self, request):
            data = request.data
            serializer = CommentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        def delete(self, request):
            data = request.data
            pk = data.get('pk')
            try:
                comment = Comment.objects.get(pk=pk)
            except Comment.DoesNotExist:
                return Response({"message: Error"}, status=status.HTTP_400_BAD_REQUEST)
            comment.delete()
            return Response({"message: o'chirildi"}, status=status.HTTP_204_NO_CONTENT)

class MovieActorAPIView(APIView):
    def get(self, pk, request):
        movies = Movie.objects.get(id=pk)
        serializers = MovieSerializer, ActorSerializer(movies.actors.all(), many=True)
        return Response(data=serializers.data)"""













"""actor_id = request.data.get('actor_id') # JSON  dan actor_id olish
        actor_id = self.request.query_params.get('actor_id') #localhost:8000/movies/1/add_actor/?actor_id=4
        actor = Actor.objects.get(id=actor_id)
        movie.actors.add(actor)"""

"""serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            actor = serializer.save()
            movie.add(actor)
            movie.add_actor(serializer.validated_data['actor'])
        return Response({'status': 'actor added'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)"""
class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["imdb", "-imdb"]

    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Movie.objects.annotate(similarity=TrigramSimilarity('name', query)).filter(
                similarity__gt=0.1).order_by('-similarity')
        return queryset

    @action(detail=True, methods=["GET"])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs): #add actor 1 usul
        movie = self.get_object()
        data = request.data
        serializer = ActorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        actor = serializer.save()
        movie.actors.add(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)


    """@action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs): #add_actor 2 usul
        movie = self.get_object()
        actor_id = self.request.query_params.get('actor_id')
        actor = Actor.objects.get(id=actor_id)
        movie.actors.add(actor)
        return Response({'status': 'actor added'})"""

    @action(detail=True, methods=["DELETE", "GET"]) #remove_actor 1 chi usul
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = self.request.query_params.get('actor_id')
        actor = Actor.objects.get(id=actor_id)
        movie.actors.remove(actor)
        return Response({'status': 200, 'message': "o'chirildi"})


    """@action(detail=True, methods=["DELETE", "GET"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        actor = Actor.objects.get(id=actor_id)
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            movie.remove(actor)
            movie.remove_actor(serializer.validated_data['actor'])
        return Response({'status': 200, 'message': "o'chirildi"})"""





class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

from django.contrib.postgres.search import TrigramSimilarity

