import requests


def get_lyrics(track, artist):
    url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&"
    api_call = (url + "q_track={}&q_artist={}&apikey=f5663a66121c1356cfb740f5e52262b3").format(
        track, artist)

    lyrics = requests.get(api_call).json()
    return lyrics['message']['body']['lyrics']['lyrics_body']
