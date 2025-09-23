import requests
from django.shortcuts import render

# Replace with your Jamendo API key

# client_id = 'your_client_id'
# client_secret = 'your_client_secret'

# token_url = "https://api.jamendo.com/v3.0/oauth/access_token"

API_KEY = ''
API_URL = 'https://api.jamendo.com/v3.0/tracks/'

def get_tracks_by_mood(request):
    mood = request.GET.get('mood', 'chill')  # Default mood is 'chill'

    # Define parameters for the API request
    params = {
        'client_id': API_KEY,
        'tags': mood,  # Using the mood as a tag to filter tracks
        'limit': 10,  # Limit the number of tracks to 10
        'format': 'json',  # Get data in JSON format
    }

    # Make the GET request to the Jamendo API
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        tracks = response.json()['results']
    else:
        tracks = []

    return render(request, 'music/mood_music.html', {'tracks': tracks})
