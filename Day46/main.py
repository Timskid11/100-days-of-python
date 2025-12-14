from bs4 import BeautifulSoup
import requests,os,spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import spotipy.oauth2 as oauth2

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header,timeout=10,allow_redirects=True)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


CLIENT_ID = 'ce0e0012954e41db99c88820771a94fa'
CLIENT_SECRET='f7bd12b7b38c416ba66f1578141206fb'
URL = 'https://ng.linkedin.com/in/timilehin-oyinlola-228296317'
SCOPE = 'playlist-modify-private'


sp_oauth = oauth2.SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=URL,scope=SCOPE)

token_info = sp_oauth.get_access_token(as_dict=False)

sp = spotipy.Spotify(auth=token_info)
current_user = sp.current_user()


current_user_id = current_user['id']
year = date.split("-")[0]
track_uris = []
for name in song_names:

    query = f"track: {name} year: {year}"
    search_results = sp.search(q=query, type='track', limit=1)

    try:
        uri = search_results["tracks"]["items"][0]["uri"]
        track_uris.append(uri)


    except Exception as e:
        print(f"{name} doesn't exist on Spotify.Skipped!!")

playlist_name = f"{date} Billboard 100"
new_playlist = sp.user_playlist_create(user=current_user_id,name=playlist_name,public=False,description=playlist_name)

playlist_id = new_playlist['id']

sp.playlist_add_items(playlist_id=playlist_id,items=track_uris)