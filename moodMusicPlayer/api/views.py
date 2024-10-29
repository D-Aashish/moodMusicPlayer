from django.http import JsonResponse
from django.shortcuts import render
# from .spotify_utils import fetch_spotify_genres
import requests
from dotenv import load_dotenv
import os 
from .spotify_utils import get_songs, get_token, search, search_songs
from mood.models import Moods

# SPOTIFY_TOKEN = os.environ.get('CLIENT_ID')

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

def fetch_categories():
    url = 'https://api.spotify.com/v1/browse/categories'
    headers = {'Authorization': f'Bearer {SPOTIFY_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def fetch_tracks(category_id):
    url = f'https://api.spotify.com/v1/browse/categories/{category_id}/playlists'
    headers = {'Authorization': f'Bearer {SPOTIFY_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def categories_view(request):
    categories = fetch_categories()
    return render(request, 'musicapp/categories.html', {'categories': categories})

def tracks_view(request, category_id):
    tracks = fetch_tracks(category_id)

def spotify(request):
    return render(request, 'api/spotify_sdk.html')

def sdk(request):
    return render(request, 'api/sdk.html')

def song_url(request):
    token = get_token(client_id, client_secret)
    result = search(token,"Ed Sheeran")
    artistId = result["id"]
    url = get_songs(token, artistId)
    return render(request,'api/song.html', {'audio_url':url})

def getsong(request):
    selected_mood_type = request.session.get('selected_mood', None)
    # retrieve the selected mood from the session
    mood_instance = None

    if selected_mood_type:
        token = get_token(client_id, client_secret)
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        music_info = search_songs(token,mood_instance)
        # music_info = search_songs(token, selected_mood)
        return render(request, 'api/search.html', {'musicInfo': music_info})
    # else:
        # return render(request, 'api/search.html', {'musicInfo': music_info})
def check_session(request):
    # Print all session data
    print(request.session.items())  # This will display all session keys and values
    
    # Specifically check for 'selected_mood'
    selected_mood = request.session.get('selected_mood', None)
    print(f"Selected Mood: {selected_mood}")  # Display the selected mood

    return render(request, 'api/check_session.html', {'selected_mood': selected_mood})

def check_mood_in_database(request):
    selected_mood_type = request.session.get('selected_mood', None)
    
    if selected_mood_type:
        # Query the database for the mood
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        
        if mood_instance:
            mood_exists = True
        else:
            mood_exists = False
    else:
        mood_exists = False  # No mood selected in session

    return render(request, 'api/check_mood.html', {
        'mood_exists': mood_exists,
        'selected_mood': selected_mood_type,
    })




# def get_spotify_genres(request):
#     access_token = '1POdFZRZbvb...qqillRxMr2z'  # Replace with your token
#     genres = fetch_spotify_genres(access_token)
#     return JsonResponse(genres)

# def get_track(request, track_id):
#     # Set the URL and the authorization token
#     url = f'https://api.spotify.com/v1/tracks/{track_id}'
#     headers = {
#         'Authorization': 'Bearer NgCXRK...MzYjw'
#     }

#     # Make the GET request
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         track_data = response.json()  # Parse the JSON response
#         return JsonResponse(track_data)  # Return the data as JSON
#     else:
#         return JsonResponse({'error': response.text}, status=response.status_code)
    # return render(request, 'musicapp/tracks.html', {'tracks': tracks})