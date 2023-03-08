from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

load_dotenv()

##Get the client id and client secret from the .env file
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

##Initialize the spotipy object, verify the scope and redirect uri
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))

##Initialize the offset to 0
first_offset = 0
i= 1

##Inizialice an empty list to store the song ids
song_ids = list()

##The maximum number of saved songs that can be retrieved is 50, so we need to loop until we get all the songs
while True:
    results = sp.current_user_saved_tracks(limit=50, offset=first_offset)  
    song_ids.extend([item['track']['id'] for item in results['items']])
    
    

    ##Print the first 50 saved songs 
    for item in results['items']:
        track = item['track']
        
        print(i) ##Song number
        print(str(item['added_at'])) ##Date when the song was added
        print(track['name'] + ' - ' + track['artists'][0]['name']) ##Song name and the artist name
        print(track['id']) ##Song id
        i=i+1
    
    ##Check if there are more than 50 songs and increment the offset by 50    
    if len(results['items']) == 50:
        first_offset = first_offset + 50 
    else: break   





