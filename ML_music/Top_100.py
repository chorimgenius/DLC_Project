import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
from musics.models import Music
from bs4 import BeautifulSoup
import requests


def Top_100_list():

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="", client_secret="")) 
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    response = requests.get('https://www.melon.com/chart/index.htm',headers=header)
    

    html = response.text
    #BeautifulSoup import
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all("div",{"class":"ellipsis rank01"})  # 노래제목

    singer = soup.find_all("div",{"class":"ellipsis rank02"}) # 가수


    real_title = []
    real_singer = []

    for i in title:
        real_title.append(i.find('a').text)

    for j in singer:
        real_singer.append(j.find('a').text)
        


    rank = 15
    results = []



    for r in range(rank):
        
        # 검색하는 경우
        search_result = sp.search(real_title[r],1,0,"track",market='KR')
        name = search_result["tracks"]["items"][0]["name"]
        music_image = search_result["tracks"]["items"][0]["album"]["images"][1]["url"]
        album = search_result["tracks"]["items"][0]["album"]["name"]
        year = search_result["tracks"]["items"][0]["album"]["release_date"][:4]
        artist = search_result["tracks"]["items"][0]["album"]["artists"][0]["name"]
        try:
            Music.objects.get(name=name)
            pass
        except:
            music = Music()
            music.name = name
            music.music_image = music_image
            music.album = album
            music.year = year
            music.artists = artist
            
            music.save()
        results.append(Music.objects.get(name=name)

    return results