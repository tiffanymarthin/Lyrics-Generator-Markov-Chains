import configparser
import requests

# Gets token from config.ini file
def getAccessToken():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_Access_Token']['token']

token = getAccessToken()

def searchMusicArtist(name):
    api_url = "https://api.genius.com/search?q={}".format(name)
    headers = {"authorization": token}
    r = requests.get(api_url, headers=headers)
    return r.json()

def getArtistID(name):
    r = searchMusicArtist(name)
    id = r["response"]["hits"][0]["result"]["primary_artist"]["id"]
    return id

def getTopTenSongs(name):
    id = getArtistID(name)
    api_url = "https://api.genius.com/artists/{}/songs".format(id)
    headers = {"authorization": token}
    params = {
        "sort": "popularity",
        "per_page": 10
    }
    r = requests.get(api_url, headers=headers, params=params)
    return r.json()

def getLyricsArray(name):
    r = getTopTenSongs(name)
    songs = r["response"]["songs"]
    lyrics_array = []
    for song in songs:
        lyrics_array.append(song["url"])
    return lyrics_array

print(getLyricsArray("sia"))