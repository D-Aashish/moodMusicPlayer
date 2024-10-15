# spotify_utils.py
import requests

def fetch_spotify_genres(access_token):
    url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.status_code, 'message': response.text}
