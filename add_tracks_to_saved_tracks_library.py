from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

##Load the .env file, which contains the client id and client secret of the spotify developer account
load_dotenv()

##Get the client id and client secret from the .env file
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

##Initialize the spotipy object, verify the scope and redirect uri
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-modify"))


tracking = ['spotify:track:6DXLO8LndZMVOHM0wNbpzg']

results = sp.current_user_saved_tracks_add(tracks=tracking)

print('Added tracks to saved tracks library')
