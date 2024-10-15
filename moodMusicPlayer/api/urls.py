# urls.py
from django.urls import path
from .views import get_spotify_genres

urlpatterns = [
    path('spotify-genres/', get_spotify_genres, name='spotify-genres'),
]
