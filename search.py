import Song
import lyrics as get_lyrics
from config import spotify


def parse_data(result):
    data = result['tracks']['items']

    for item in data:

        track_id = item['id']

        artist_id = item['album']['artists'][0]['id']
        artist_details = spotify.artist(artist_id)

        album_tracks = spotify.album_tracks(item['album']['id'])
        album_track = []

        album_recommendations = []

        recommendations = spotify.recommendations(seed_tracks=["{}".format(track_id)], limit=4)
        for r in recommendations['tracks']:
            album_recommendations.append({
                "album_art": r['album']['images'][0]['url'],
                "album_name": r['album']['name'],
                "name": r['name'],
                "url": r['external_urls']['spotify']
            })

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
            "art": item['album']['images'][1]['url'],
            "tracks": album_track,
            "recommendations": album_recommendations
        }

        track = {
            "name": item['name'],
            "url": item['external_urls']['spotify'],
            'popularity': item['popularity'],
            "id": track_id
        }

        lyrics = get_lyrics.get_lyrics(track['name'], artist['name'])

    track_details = Song.Song(artist_name=artist['name'], artist_image=artist['image'],
                              album_name=album['name'], album_art=album['art'], album_tracks=album['tracks'],
                              track_name=track['name'], url=track['url'], popularity=track['popularity'],
                              id=track['id'], recommendations=album['recommendations'], lyrics=lyrics)

    return track_details


def search(user_input):
    return parse_data(spotify.search(q=user_input, limit=1, type='track'))
