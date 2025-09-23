import requests

# Jamendo API credentials
client_id = '34dc722e'  # Replace with your actual client_id from Jamendo

# The URL for fetching artist's tracks with given filters
url = f"https://api.jamendo.com/v3.0/artists/tracks/"
mood_genre_map = {
    'happy': ['pop', 'dance', 'upbeat'],
    'sad': ['blues', 'melancholic', 'slow'],
    'angry': ['rock', 'metal', 'intense'],
}

selected_mood = 'happy'  # Example user-selected mood
selected_genres = mood_genre_map[selected_mood]

# Now search using those genres as tags
for genre in selected_genres:
    params = {
        'client_id': client_id,
        'format': 'jsonpretty',
        'tags': genre,  # Pass the relevant genre as tag
        'order': 'track_name_desc',
        # 'limit': 10
    }
    response = requests.get(url, params=params)

# Parameters to send the request
# params = {
#     'client_id': client_id,
#     'format': 'jsonpretty',   # Pretty JSON format
#     'order': 'track_name_desc',  # Order by track name in descending order
#     'name': 'joy',      # Search for tracks related to 'we are fm'
#     'album_datebetween': '0000-00-00_2025-01-01'  # Filter tracks based on album release date range
# }

# Send the GET request to the Jamendo API
# response = requests.get(url, params=params)

# Check the response status and print the result
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Check if 'results' contains tracks
    if data.get('results'):
        print("Fetched Tracks:", data['results'])
    else:
        print("No tracks found based on the given parameters.")
else:
    print(f"Failed to fetch tracks. Status code: {response.status_code}")
    print("Raw Response:", response.text)
