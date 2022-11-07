import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
from musics.models import Music
from bs4 import BeautifulSoup
import requests


def Top_100_list():

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="", client_secret=""))    
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    response = requests.get('https://www.melon.com/chart/index.htm',headers=header) #멜론차트는 헤더정보를 입력해줘야함
    

    html = response.text
    #BeautifulSoup import
    soup = BeautifulSoup(html, 'html.parser')    #html.parser를 사용해서 soup에 넣겠다

    title = soup.find_all("div",{"class":"ellipsis rank01"})  #노래제목

    singer = soup.find_all("div",{"class":"ellipsis rank02"}) #가수


    real_title = []
    real_singer = []

    for i in title:
        real_title.append(i.find('a').text)

    for j in singer:
        real_singer.append(j.find('a').text)
        


    rank = 15 # 여기서 몇 위까지 띄울 예정인지 (최대:100위)
    results = [] # Music [1위] [2] [3] [4] [5]



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
            music.name = name # 여기서 DB저장을 할 수 있을까요?? 아니면 이거를 IMPORT 해서 views.py에서 작성을 해서 DB에 저장을 해야 할까요?
            music.music_image = music_image
            music.album = album
            music.year = year
            music.artists = artist
            
            music.save()
        results.append(Music.objects.get(name=name)) # recommend_song 결과값을 넣어서 비슷하게 result를 만들어서? 함수를 또 하나 짜서??? 하면되는데 

    return results