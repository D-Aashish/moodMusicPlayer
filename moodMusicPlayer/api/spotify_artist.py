import requests
import os

# The artist ID you want to retrieve information for
artist_id = '6eUKZXaKkcviH0Ku9w2n3V'
# Your access token
access_token = os.environ.get("ACCESS_TOKEN")

# Set up the request URL
url = f"https://api.spotify.com/v1/artists/{artist_id}"

# Set up the headers, including the Authorization header
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check for a successful response
if response.status_code == 200:
    artist_info = response.json()
    print(artist_info)  # Print the full response
else:
    print(f"Error: {response.status_code} - {response.text}")


# {'external_urls': {'spotify': 'https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V'},
#  'followers': {'href': None, 'total': 116608651},
#  'genres': ['pop', 'singer-songwriter pop', 'uk pop'],
#  'href': 'https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V',
#  'id': '6eUKZXaKkcviH0Ku9w2n3V',
#  'images': [{'url': 'https://i.scdn.co/image/ab6761610000e5eb784daff754ecfe0464ddbeb9',
#  'height': 640, 'width': 640},
#  {'url': 'https://i.scdn.co/image/ab67616100005174784daff754ecfe0464ddbeb9',
#      'height': 320, 'width': 320},
#  {'url': 'https://i.scdn.co/image/ab6761610000f178784daff754ecfe0464ddbeb9',
#     'height': 160, 'width': 160}],
#    'name': 'Ed Sheeran',
#     'popularity': 89,
#     'type': 'artist',
#     'uri': 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V'}