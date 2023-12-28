import spotipy
import pytube

# Authenticate with Spotify API (replace with your credentials)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='your_client_id', client_secret='your_client_secret'))

# Get song information from Spotify link
song_link = input("Enter Spotify song link: ")
track = sp.track(song_link)
title = track['name']
artist = track['artists'][0]['name']

# Search for the song on YouTube
yt = pytube.YouTube("https://www.youtube.com/results?search_query=" + title + " " + artist)

# Download the highest quality audio stream
yt.streams.filter(only_audio=True).order_by('abr').desc().first().download()
