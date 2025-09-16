import base64
from dotenv import load_dotenv , set_key
# import json
import os
import requests  
import logging

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(main_dir, '.env')

# Load environment variables from .env file
load_dotenv(dotenv_path)

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

def validate_client_credentials(client_id, client_secret):
    """Validate that the client_id and client_secret are properly set."""
    if not client_id or not isinstance(client_id, str) or not client_id.strip():
        raise ValueError("Missing or invalid client ID: Make sure it's loaded properly.")
    if not client_secret or not isinstance(client_secret, str) or not client_secret.strip():
        raise ValueError("Missing or invalid client secret: Make sure it's loaded properly.")

def store_access_token(access_token):
    # access_token = access_token.get('access_token')
    if access_token:
        try:
            os.environ['ACCESS_TOKEN'] = access_token
            set_key(dotenv_path, 'ACCESS_TOKEN', access_token)
            with open('access_token.txt', 'w') as token_file:
                    token_file.write(access_token)
        except Exception as e:
            print(f"An error occurred while storing the token: {e}")
    else:
        print(f"the token {access_token} is invalid please check again")

def get_token(client_id, client_secret):
    validate_client_credentials(client_id, client_secret)
    auth_string = f"{client_id.strip()}:{client_secret.strip()}"
    auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode()
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {auth_base64}',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Will raise an HTTPError if the response code is 4xx/5xx
        response_data = response.json()
        access_token = response_data.get('access_token')
        if access_token:
            logging.info("Access token obtained successfully.")
            return access_token
        else:
            logging.error("Access token not found in the response.")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting token: {e}")
        return None

def get_auth_header(token):
    if not token:
        raise ValueError("Invalid or missing Spotify token.")
    if isinstance(token, dict) and 'access_token' in token:
        return {"Authorization": "Bearer " + token['access_token']}
    elif isinstance(token, str):
        return {"Authorization": "Bearer " + token}
    else:
        raise ValueError("Invalid Spotify token format.")

def search(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    try:
        result = requests.get(url, headers=headers, params=params)
        result.raise_for_status()
        result_data = result.json().get("artists", {}).get("items", [])
        return result_data[0] if result_data else None
    except requests.exceptions.RequestException as e:
        print(f"Error searching artist: {e}")
        return None

# def search_songs(token, mood):
#     print("Searching Spotify for mood:", mood)
#     url = "https://api.spotify.com/v1/search"
#     print("spotify token: ",token)
#     headers = get_auth_header(token)
#     # print("headers :",headers )
#     # if not headers:
#     #     print("Error: Invalid headers")
#     # return []
#     # query = f"?q={artist_name}&type=artist&limit=1"
#     query= f"?q={mood}&type=track"
#     query_url = url + query
#     print("this is the result")
#     result = requests.get(query_url, headers=headers)
#     print("result: ", result)
#     try:
#         result.raise_for_status()
#         result_data = result.json().get("tracks", {}).get("items", [])
#         # if not result_data:
#         #     print("No songs found for this mood.")
#         # return []
#         song_info_list = []
        
#         print("for loop staring")
#         for track in result_data:
#             print("preview url", track.get("preview_url"))
#             if track.get("preview_url"):
#                 song_info = {
#                     "title": track["name"],
#                     "artist": ", ".join(artist["name"] for artist in track["artists"]),
#                     "album": track["album"]["name"],
#                     # "image_url": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
#                     "preview_url": track["preview_url"]
#                 }
#                 song_info_list.append(song_info)
#             # print("this is song_info",song_info)
#         return song_info_list
#         print("for loop ending")
#     except requests.exceptions.RequestException as e:
#         print(f"Error searching songs: {e}")
#         return []

def search_songs(token, mood):
    print("Searching Spotify for mood:", mood)
    url = "https://api.spotify.com/v1/search"
    print("spotify token: ", token)
    headers = get_auth_header(token)
    
    query = f"?q={mood}&type=track&limit=1"
    query_url = url + query
    print("Query URL:", query_url)

    result = requests.get(query_url, headers=headers)
    print("Result status:", result.status_code)
    
    try:
        result.raise_for_status()
        result_data = result.json().get("tracks", {}).get("items", [])
        # print("Result data:", result_data)
        
        if not result_data:
            print("No songs found for this mood.")
            return []
        
        song_info_list = []
        
        for track in result_data:
            # Check if a preview URL exists
            if track.get("preview_url"):
                song_info = {
                    "title": track["name"],
                    "artist": ", ".join(artist["name"] for artist in track["artists"]),
                    "album": track["album"]["name"],
                    "preview_url": track["preview_url"],
                    "album_image": track["album"]["images"][0]["url"] if track["album"]["images"] else None
                }
                song_info_list.append(song_info)
                print("preview of if" ,song_info_list.append(song_info))
            else:
                # Handle tracks without a preview URL (optional)
                song_info = {
                    "title": track["name"],
                    "artist": ", ".join(artist["name"] for artist in track["artists"]),
                    "album": track["album"]["name"],
                    "preview_url": "No preview available",
                    "album_image": track["album"]["images"][0]["url"] if track["album"]["images"] else None
                }
                song_info_list.append(song_info)
                print("preview of else" ,song_info)

        return song_info_list
    except requests.exceptions.RequestException as e:
        print(f"Error searching songs: {e}")
        return []


def get_songs(token , artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=IS"
    headers = get_auth_header(token)
    result = requests.get(url,headers=headers)
    result_data = result.json()
    # return result_data
    try:
        result.raise_for_status()
        return result.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting top tracks: {e}")
        return None


token = get_token(client_id, client_secret)

mood= "HAPPY"
song = search_songs(token, mood)
print("song: ",song)
