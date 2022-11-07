import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
from musics.models import Music
from user.models import User
from ML_music.music_rc import recommend_songs


def recommend_music(id): # 어떤 정보를 담아서 넣을 것이다.

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="", client_secret=""))    
    re_song = 10 # # recommend_song 결과물 {'name' : 'Nxde','artists':'idle'}

    # views.py 에서 필요한 형태로 Music Model 형태
    results = [] # Music [1위] [2] [3] [4] [5]

    # User id=id
    user = User.objects.get(id=id)
    musics2 = user.likes_music.all()
    # pprint(f"내 곡 리스트 : {musics2}") # 쿼리셋이란게 list란 뜻!
    
    song_list = []
    for music in musics2: # music = Music
        song_list.append({'name':music.name,'year':int(music.year)})
        
    results = recommend_songs(song_list) # 10개
    results_return = []
    for result in results:
        search_result = sp.search(result['name'],1,0,"track",market='KR')
        name = search_result["tracks"]["items"][0]["name"]
        music_image = search_result["tracks"]["items"][0]["album"]["images"][1]["url"]
        album = search_result["tracks"]["items"][0]["album"]["name"]
        year = search_result["tracks"]["items"][0]["album"]["release_date"][:4]
        artist = search_result["tracks"]["items"][0]["album"]["artists"][0]["name"]
        try:
            Music.objects.get(name=name)
        except:
            search_result = sp.search(result['name'],1,0,"track",market='KR')
            music = Music()
            music.name = name # 여기서 DB저장을 할 수 있을까요?? 아니면 이거를 IMPORT 해서 views.py에서 작성을 해서 DB에 저장을 해야 할까요?
            music.music_image = music_image
            music.album = album
            music.year = year
            music.artists = artist
            music.save()

        results_return.append(Music.objects.get(name=name))
    return results_return
    