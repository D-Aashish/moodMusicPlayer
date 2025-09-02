from django.http import JsonResponse
from django.shortcuts import render
# from .spotify_utils import fetch_spotify_genres
import requests
from dotenv import load_dotenv
import os 
from .spotify_utils import get_songs, get_token, search, search_songs
from mood.models import Moods

SPOTIFY_TOKEN = os.environ.get('CLIENT_ID')  

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
    # error is showing in this line but i don't know what is causing this error it might be caused due to specifically writting name of artist
    result = search(token,"Ed Sheeran")
    artistId = result["id"]
    url = get_songs(token, artistId)
    return render(request,'api/song.html', {'audio_url':url})

def getsongView(request):
    selected_mood_type = request.session.get('selected_mood', None)
    spotify_token = request.session.get('spotify_token', None)
    print("Selected Mood from session:", selected_mood_type)
    print("Spotify Token from session:", spotify_token)
    # retrieve the selected mood from the session
    mood_instance = None
    music_info = []

    if selected_mood_type and spotify_token:
        # retrieve token from .env
        token_data = get_token(client_id, client_secret)
        # mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        # print("Mood instance found:", mood_instance)
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        print("Mood instance found:", mood_instance)

        if token_data and 'access_token' in token_data:
            token = token_data['access_token']
        #     mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        #     print("Mood instance found:", mood_instance)

        if mood_instance:
                    music_info = search_songs(token, mood_instance.type)
                    print("Fetched songs:", music_info)
                # music_info = search_songs(token,mood_instance)
        else:
                    # music_info = []
                    print("No mood instance found.")
    else:
        print("❌ Missing selected mood or Spotify token in session.")
        if not spotify_token:
            music_info = [{'error': 'Spotify access token is missing from the session. Please try again.'}]
        else:
            music_info = [{'error': 'Selected mood is missing from the session.'}]

            
        context = {
           'musicInfo': music_info,
        #    'indices': range(len(music_info))  # Create a range of indices
        }
        # music_info = search_songs(token, selected_mood)
        return render(request, 'api/search1.html', context)

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


def youtube_play(request):
    return render(request, 'api/yplay.html')

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