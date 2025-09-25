# import base64
# from dotenv import load_dotenv , set_key
import json
import os
import requests  
# import logging

# main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# dotenv_path = os.path.join(main_dir, '.env')

# # Load environment variables from .env file
# load_dotenv(dotenv_path)

client_id = os.environ.get("CLIENT_ID")
# client_secret = os.environ.get("CLIENT_SECRET")

def fetch_songs_from_jamendo(mood):
    print("spotify_utils mood:", mood)
    # mood = mood.type
    url = f"https://api.jamendo.com/v3.0/tracks/"
    mood_genre_map = {
            'HA': ['pop', 'dance', 'upbeat'],
            'EX': ['electronic', 'dance'],
            'CA': ['ambient', 'chill', 'lofi'],
            'GR': ['acoustic', 'folk'],
            'HOL': ['uplifting', 'positive'],
            'SA': ['blues', 'slow', 'melancholic'],
            'AN': ['rock', 'metal', 'intense'],
            'ANX': ['calm', 'ambient', 'relaxing'],
            'BO': ['indie', 'alternative'],
            'LO': ['soft', 'emotional'],
            'NI': ['neutral', 'instrumental'],
            'PE': ['pensive', 'acoustic'],
            'NO': ['nostalgic', 'retro'],
            'BI': ['bittersweet', 'melancholic'],
            'AM': ['ambivalent', 'mixed'],
            'RO': ['romantic', 'love'],
            'PL': ['playful', 'fun'],
            'ME': ['melancholic', 'slow'],
            'MO': ['motivational', 'energetic'],
            'FR': ['frustrated', 'intense'],
            'TI': ['tiring', 'slow'],
            'EN': ['energetic', 'dance'],
            'SP': ['spiritual', 'calm'],
            'EXH': ['exhilarated', 'upbeat'],
            'HOS': ['hopeless', 'slow'],
            'FA': ['faithful', 'calm'],
            'AW': ['awkward', 'quirky'],
            'CO': ['confident', 'strong'],
            'SU': ['surprised', 'fun'],
            'DI': ['disappointed', 'slow'],
            'FO': ['forgiving', 'soft'],
    }
    genres = mood_genre_map.get(mood, [mood.lower()])
    tags = ",".join(genres)
    # tags = mood
    print("Tags being searched for:", tags)
    params = {
            'client_id': client_id,
            'format': 'jsonpretty',
            'limit': 2,
            'fuzzytags': tags,
            "order": "popularity_total",
            "include": "musicinfo",
            "groupby": "artist_id"
        }
    response = requests.get(url, params=params)
    print("url" , response.url)

    if response.status_code == 200:
        data = response.json()
        print("Raw API data:", json.dumps(data, indent=2))
        results = data.get("results", [])
        if results:
                print("First track example:", json.dumps(results[0], indent=2))
                return results
        else:
                print("No tracks found based on the given parameters.")
    else:
        print(f"Failed to fetch tracks. Status code: {response.status_code}")
        print("Raw Response:", response.text)
    # try:
    #     result.raise_for_status()
    #     result_data = result.json().get("tracks", {}).get("items", [])
        
    #     if not result_data:
    #         print("No songs found for this mood.")
    #         return []
        
    #     song_info_list = []
        
    #     for track in result_data:
    #         song_info = {
    #             "title": track["name"],
    #             "artist": ", ".join(artist["name"] for artist in track["artists"]),
    #             "album": track["album"]["name"],
    #             "preview_url": track["preview_url"] if track["preview_url"] else "No preview available",
    #             "album_image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
    #             # Provide the direct Spotify URL for the track (not URI)
    #             "spotify_url": track["external_urls"]["spotify"]  # Full URL for the song on Spotify
    #         }
    #         song_info_list.append(song_info)

    #     return song_info_list
    # except requests.exceptions.RequestException as e:
    #     print(f"Error searching songs: {e}")
    #     return []
