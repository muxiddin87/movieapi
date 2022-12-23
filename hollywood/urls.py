from django.urls import path, include
from .views import MovieViewSet, ActorViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [

    path('', include(router.urls)),


            ]

from rest_framework.authtoken import views

    #path('comments/', CommentAPIView.as_view(), name='comments'),
    #path('auth/', views.obtain_auth_token),
    #path('movies/<int:id>/actors', MovieActorAPIView.as_view(), name='movies/id/actors'),
