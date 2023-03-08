from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id,client_secret)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-read-private"))

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))
        

playlists = sp.current_user_playlists()
user_id = sp.me()['id']
print(user_id)
for playlist in playlists['items']:
    if playlist['owner']['id'] == user_id:
        print()
        print(playlist['name'])
        print('  total tracks', playlist['tracks']['total'])

        results = sp.playlist(playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)

        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)

