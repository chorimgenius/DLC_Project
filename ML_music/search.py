import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
from musics.models import Music
from user.models import User
from ML_music.music_rc import recommend_songs


def search_music(search_title): 

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="471f5ad097d044e688c2318eb88bd7f2", client_secret="b8cbdaf1d6c04466af872f64d39df16f"))
    search_result = sp.search(search_title,1,0,"track",market='KR')
    name = search_result["tracks"]["items"][0]["name"]
    music_image = search_result["tracks"]["items"][0]["album"]["images"][1]["url"]
    album = search_result["tracks"]["items"][0]["album"]["name"]
    year = search_result["tracks"]["items"][0]["album"]["release_date"][:4]
    artist = search_result["tracks"]["items"][0]["album"]["artists"][0]["name"]

    try:
        Music.objects.get(name=name)

    except:
        music = Music()
        music.name = name
        music.music_image = music_image
        music.album = album
        music.year = year
        music.artists = artist
            
        music.save()

    return  Music.objects.get(name=name)
