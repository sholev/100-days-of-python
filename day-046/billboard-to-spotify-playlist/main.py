from dotenv import dotenv_values
import billboard
import spotify

config = dotenv_values("../../.env")

date = input("Enter date for playlist (YYYY-MM-DD):")
if len(date) == 0:
    date = "2000-08-12"

song_list = billboard.get_song_list(date)
spotify_token = spotify.get_access_token()
track_ids = []
for song in song_list:
    track = song['track']
    artist = song['artist']
    search_query = f"track:\"{track}\" artist:\"{artist}\""
    track_id = spotify.search_song(spotify_token, search_query)
    if track_id:
        track_ids.append(track_id)
        print(f"ID: {track_id} for  '{song}' added.")
    else:
        track = song['track']
        search_query = f"track:\"{track}\""
        track_id = spotify.search_song(spotify_token, search_query, "track")
        if track_id:
            track_ids.append(track_id)
            print(f"ID: {track_id} for  '{song}' added.")
        else:
            print(f">>>> '{song}' not found.")

data = spotify.exchange_code_for_tokens(config["SPOTIFY_CODE"])
playlist_id = spotify.create_playlist(data["access_token"],
                                      config["SPOTIFY_USERNAME"],
                                      f"Billboard top 100 for {date}")
spotify.add_songs_to_playlist(data["access_token"], playlist_id, track_ids)
