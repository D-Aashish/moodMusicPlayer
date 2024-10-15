# views.py
from django.http import JsonResponse
from .spotify_utils import fetch_spotify_genres

def get_spotify_genres(request):
    access_token = '1POdFZRZbvb...qqillRxMr2z'  # Replace with your token
    genres = fetch_spotify_genres(access_token)
    return JsonResponse(genres)
