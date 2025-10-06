import json
import os
import requests  
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("CLIENT_ID")

def fetch_songs_from_jamendo(mood):
    print("spotify_utils mood:", mood)
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
    params = {
            'client_id': client_id,
            'format': 'jsonpretty',
            'limit': 5,
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

def getTopArtist():
        url = f"https://api.jamendo.com/v3.0/artists/"
        params = {
            'client_id': client_id,
            'format': 'jsonpretty',
            'limit': 10,
            "order": "popularity_total",
        }

        response = requests.get(url, params=params)
        # print("url" , response.url)
        if response.status_code == 200:
                data = response.json()
                # print("Raw API data:", json.dumps(data, indent=2))
                results = data.get("results", [])
                if results:
                        # print("First track example:", json.dumps(results[0], indent=2))
                        return results
                else:
                        print("No artist found based on the given parameters.")
        else:
                print(f"Failed to fetch tracks. Status code: {response.status_code}")
                print("Raw Response:", response.text)