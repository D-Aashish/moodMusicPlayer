# spotify_utils.py
import requests
import base64
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token(CLIENT_ID, CLIENT_SECRET):
    auth_string = f"{CLIENT_ID }:{CLIENT_SECRET}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    # Set up the request
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {encoded_auth}',
        'Content-tyoe': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    # Make the POST request
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        return response_data
    else:
        print(f"Error: {response.status_code} - {response.text}")


token = get_token(CLIENT_ID, CLIENT_SECRET)
    # Access Token: BQBmyWWTwroTAib7_uiwor1v7bDvp2DYv4U7XSGlHJH1QYtQDCfkkrH4RvZFGemy_bRsv9kjljnqKVHLIpsbbGB5ApwIpInexyf3iJINs1O_E9nu6bY
    # {'access_token': 'BQBgxoQuAwi_mHuHmpkwoK04ziJ_4I-rwF0FcVjzZgUopOhK9Zcc4kngrg6lGlOiJf1D94ha2xKxjPqcHpx-ruIiegGg7H6mCob712-AfKeDBJkCRf4',
    #  'token_type': 'Bearer',
    #  'expires_in': 3600}