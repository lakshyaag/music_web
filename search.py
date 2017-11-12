import Song
from config import spotify


def parse_data(result):
    data = result['tracks']['items']

    for item in data:

        artist_id = item['album']['artists'][0]['id']
        artist_details = spotify.artist(artist_id)

        album_tracks = spotify.album_tracks(item['album']['id'])
        album_track = []
        for tracks in album_tracks['items']:
            album_track.append({
                "name": tracks['name'],
                "url": tracks['external_urls']['spotify']
            })

        artist = {
            "image": artist_details['images'][1]['url'],
            "name": artist_details['name']
        }

        album = {
            "name": item['album']['name'],
            "art": item['album']['images'][0]['url'],
            "tracks": album_track

        }

        track = {
            "name": item['name'],
            "url": item['external_urls']['spotify'],
            'popularity': item['popularity'],
            "id": item['id']
        }

    track_details = Song.Song(artist_name=artist['name'], artist_image=artist['image'],
                              album_name=album['name'], album_art=album['art'], album_tracks=album['tracks'],
                              track_name=track['name'], url=track['url'], popularity=track['popularity'],
                              id=track['id'])

    return track_details


def search(user_input):
    return parse_data(spotify.search(q=user_input, limit=1, type='track'))
