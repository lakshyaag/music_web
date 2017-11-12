from flask import Flask, render_template, request

import search

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_data():
    track = request.form['track']

    track_details = search.search(track)

    return render_template('music.html', artist_name=track_details.artist_name, album_name=track_details.album_name,
                           album_tracks=track_details.album_tracks, track_name=track_details.track_name,
                           popularity=track_details.popularity, url=track_details.url,
                           album_art=track_details.album_art, artist_image=track_details.artist_image,
                           id=track_details.id, recommendations=track_details.recommendations)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
