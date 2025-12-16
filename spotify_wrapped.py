import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
  auth_manager = SpotifyOAuth(
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET",
    redirect_uri = "http://127.0.0.1:8888/callback",
    scope = "user-top-read user-read-recently-played"
  )
)

top_tracks = sp.current_user_top_tracks(
  limit = 10,
  time_range = "long_term"
)

print("\n🎧 TOP 10 TRACKS")
for i, track in enumerate(top_tracks["items"], start = 1):
  print(f"{i}. {track['name']} - {track['artists'][0]['name']}")

top_artists = sp.current_user_top_artists(
  limit = 10,
  time_range = "long_term"
)

print("\n🎤 TOP 10 ARTISTS")
for i, artists in enumerate(top_artists["items"], start = 1):
  print(f"{i}. {artists['name']}")
