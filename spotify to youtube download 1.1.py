import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from pytube import Search

# Set up your Spotify API credentials
client_id = '5406074d160144aeba00bdb4092be110'
client_secret = 'e7d04785254746c4ab5fc0d8cf4c5e9c'

# Authenticate and authorize your application
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Specify the playlist ID
playlist_id = '37i9dQZF1DX4dyzvuaRJ0n'

# Make the API request to get the playlist tracks
playlist = sp.playlist_tracks(playlist_id)

# Extract the names of the tracks from the response
track_names = [item['track']['name'] for item in playlist['items']]

# Print the track names
print("Track Names:")
for name in track_names:
    print(name)

# Provide the video name to search for
for video_name in track_names:
    print(video_name)
    search_results = Search(video_name)
    print(search_results)
    video_url = search_results.results[0].watch_url
    print(video_url)
    yt = YouTube(video_url)
    video_stream = yt.streams.get_highest_resolution()
    output_path = "C:/Users/tejus/OneDrive/Desktop/this is vid"
    video_stream.download(output_path)


# In[ ]:





# In[ ]:





# In[ ]:




