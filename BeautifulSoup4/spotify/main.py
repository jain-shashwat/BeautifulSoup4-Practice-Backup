from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "5de0a81f59a948be8e667fab5431db69"
CLIENT_SECRET = "69baf126005b467c9f730e856d967094"



date = input("Which Date songs you would like to Add in format (YYYY-MM-DD): ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")
song_title = soup.select(selector="li h3.c-title")
song_names = [song.getText().strip() for song in song_title]

print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=True)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)





