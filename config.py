import spotipy
import spotipy.util as util

CLIENT_ID = "0344d9a7828f497298eaefbb02327f84"
CLIENT_SECRET = "680fd21219984948a49fb0bb89271d7d"

token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET).get_access_token()
spotify = spotipy.Spotify(token)
