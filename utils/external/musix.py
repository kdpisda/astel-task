import os

import requests


class MusixMatchClient:
    def __init__(self):
        self.api_key = os.getenv("MUSIXMATCH_API_KEY")
        self.base_url = "https://api.musixmatch.com/ws/1.1/"

    def get(self, url, params):
        url = f"{self.base_url}{url}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            resp_json = response.json()
            return resp_json.get("message", {}).get("body", {})
        return None

    def get_track(self, artist_name, track_name):
        url = "matcher.track_get"
        params = {
            "q_artist": artist_name,
            "q_track": track_name,
            "apikey": self.api_key,
            "format": "json",
        }
        return self.get(url, params=params)

    def get_lyrics(self, artist_name, track_name):
        url = "matcher.lyrics.get"
        params = {
            "q_artist": artist_name,
            "q_track": track_name,
            "apikey": self.api_key,
            "format": "json",
        }
        return self.get(url, params=params)
        return None
