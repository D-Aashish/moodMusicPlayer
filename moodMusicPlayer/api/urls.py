# urls.py
from django.urls import path
# from .views import categories_view, tracks_view , spotify , sdk, song_url, getsong
from .views import *

urlpatterns = [
    # path('spotify-genres/', get_spotify_genres, name='spotify-genres'),
    # path('category/', categories_view, name='categories'),
    # path('category/<str:category_id>', tracks_view, name='tracks'),
    # path('spotify', spotify, name='spotify'),
    # path('sdk', sdk, name='sdk'),
    # path('play', song_url, name='songUrl'),
    # path('search', getsongView, name='song'),
    # path('session', check_session, name='session'),
    # path('checkmood', check_mood_in_database, name='mood'),
    # path('yplay', youtube_play, name='yplay'),
]
