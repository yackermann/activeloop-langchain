from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import os, json

with open("lyrics_with_spotify_url.json", "r") as r:
    lyrics = json.loads(r)

