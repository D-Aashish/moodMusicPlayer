# from django.http import JsonResponse
from django.shortcuts import render
# # from .spotify_utils import fetch_spotify_genres
# import requests
# from dotenv import load_dotenv
# import os 
# from .spotify_utils import get_songs, get_token, search, search_songs
from .spotify_utils import fetch_songs_from_jamendo as search_songs
from mood.models import Moods

# SPOTIFY_TOKEN = os.environ.get('CLIENT_ID')  

# load_dotenv()

# client_id = os.environ.get("CLIENT_ID")
# client_secret = os.environ.get("CLIENT_SECRET")

def getsongView(request,mood_instance=None):
    selected_mood_type = request.session.get('selected_mood', None)
    # print("Selected mood from session:", selected_mood_type) 
    music_info = []
    if selected_mood_type:
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        if mood_instance:
            music_info = search_songs(mood_instance.type)
        context = {'musicInfo': music_info}
        return render(request, 'api/search1.html', context)