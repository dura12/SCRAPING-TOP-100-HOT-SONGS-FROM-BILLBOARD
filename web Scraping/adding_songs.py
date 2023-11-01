####ADDING SONGS TO OUR SPOTIFY PLAYLIST

import spotipy
from main import Songs
from spotipy.oauth2 import SpotifyOAuth

spotify_id="YOUR SPOTIFY CLIENT ID"
sec_id="YOUR SECRET ID"
SPOTIPY_REDIRECT_URI='YOUR REDIRECT URI'
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=SPOTIPY_REDIRECT_URI,
                client_id=spotify_id,
                client_secret=sec_id,
                show_dialog=True,
                cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]
def adding_songs_to_new_playlist():
        song=Songs()
        songs=song.song_lists()
        song_names=songs[0]
        year=songs[1]

        song_uris = []
        for item in song_names:
                result = sp.search(q=f"track:{item} year:{year}", type="track")
                try:
                        uri = result["tracks"]["items"][0]["uri"]
                        song_uris.append(uri)
                except IndexError:
                        print(f"{item} doesn't exist in Spotify. Skipped.")

        playlist=sp.user_playlist_create(user=user_id,name=f"top 100 billboard of year {year}",public=False)

        i=playlist['id']
        sp.playlist_add_items(playlist_id=i,items=song_uris)
adding_songs_to_new_playlist()
