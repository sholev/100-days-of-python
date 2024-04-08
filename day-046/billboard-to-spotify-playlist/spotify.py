import base64
import requests
from dotenv import dotenv_values

TOKEN_URL = "https://accounts.spotify.com/api/token"
API_URL = "https://api.spotify.com/v1/"
REDIRECT_URI = "http://example.com/"

config = dotenv_values("../../.env")


def get_authorization_code():
    scope = "playlist-modify-public playlist-modify-private"
    url = f"https://accounts.spotify.com/authorize?" \
          f"client_id={config["SPOTIFY_ID"]}&" \
          f"response_type=code&" \
          f"redirect_uri={REDIRECT_URI}&" \
          f"scope={scope}"

    r = requests.get(url)
    for redirect in r.history:
        print(redirect.url)


def get_access_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": config["SPOTIFY_ID"],
        "client_secret": config["SPOTIFY_SECRET"]
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r = requests.post(TOKEN_URL, headers=headers, data=payload)
    if r.status_code == 200:
        data = r.json()
        return data["access_token"]
    else:
        print("Error:", r.status_code, r.text)


def exchange_code_for_tokens(code):
    auth_string = f"{config["SPOTIFY_ID"]}:{config["SPOTIFY_SECRET"]}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_base64}"}
    data = {"grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI}
    r = requests.post(TOKEN_URL, headers=headers, data=data)
    if r.status_code == 200:
        data = r.json()
        print(data)
        return data
    else:
        print(f"Error exchanging code for tokens: {r.status_code} - {r.text}")
        return None


def create_playlist(access_token, user_id, playlist_name):
    url = f"{API_URL}users/{user_id}/playlists"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"name": playlist_name, "public": True}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        data = r.json()
        playlist_id = data["id"]
        print(data)
        print(f"Playlist created successfully (ID: {playlist_id})")
        return playlist_id
    else:
        print(f"Error creating playlist: {r.status_code} - {r.text}")
        return None


def add_songs_to_playlist(access_token, playlist_id, songs):
    url = f"{API_URL}playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"uris": songs}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        print(f"Songs added to playlist successfully.")
    else:
        print(f"Error adding songs to playlist: {r.status_code} - {r.text}")


def search_song(access_token, query, q_type="track,artist", attempts=1):
    if attempts < 0:
        return None

    url = f"{API_URL}search"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": query, "type": q_type}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    data = r.json()
    if data["tracks"]["total"] > 0:
        # Assuming the first result
        first_track = data["tracks"]["items"][0]
        return first_track["uri"]
    else:
        query = query.replace("'", "")
        query = query.replace("-", " ")
        return search_song(access_token, query, q_type, attempts - 1)
