from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

##Load the .env file, which contains the client id and client secret of the spotify developer account
load_dotenv()

##Get the client id and client secret from the .env file
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

scopes = [
  'ugc-image-upload',
  'user-read-playback-state',
  'user-modify-playback-state',
  'user-read-currently-playing',
  'streaming',
  'app-remote-control',
  'user-read-email',
  'user-read-private',
  'playlist-read-collaborative',
  'playlist-modify-public',
  'playlist-read-private',
  'playlist-modify-private',
  'user-library-modify',
  'user-library-read',
  'user-top-read',
  'user-read-playback-position',
  'user-read-recently-played',
  'user-follow-read',
  'user-follow-modify'
]

##Initialize the spotipy object, verify the scope and redirect uri
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=scopes,))


tracking = ['6DXLO8LndZMVOHM0wNbpzg','0oks4FnzhNp5QPTZtoet7c']

results = sp.current_user_saved_tracks_add(tracks=tracking)

print('Added tracks to saved tracks library')
