# urls.py
from django.urls import path
from .views import categories_view, tracks_view

urlpatterns = [
    # path('spotify-genres/', get_spotify_genres, name='spotify-genres'),
    path('category/', categories_view, name='categories'),
    path('category/<str:category_id>', tracks_view, name='tracks'),
]
