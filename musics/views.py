from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from musics import serializers
from musics.models import Music
from musics.serializers import MusicSerializer, MusicListSerializer, MusicDetailSerializer
from review.models import Review
from ML_music.Top_100 import Top_100_list
from ML_music.search_music import recommend_music
from review.serializers import ReviewSerializer

# Create your views here.
class MusicListView(APIView):
    def get(self, request):
        
        # top10 list
        musics = Top_100_list()
        top10_serializer = MusicListSerializer(musics,many=True)

        # 내 곡 list
        user = self.request.user
        musics2 = user.likes_music.all()
        my_list_serializer = MusicListSerializer(musics2, many=True)
        
        # 추천 곡 list
        response_data = []
        response_data.append(top10_serializer.data)
        response_data.append(my_list_serializer.data)
        if musics2.count() == 0:
            response_data.append(top10_serializer.data) # top10
        else:
            music_recommend = recommend_music(request.user.id)
            recommend_serializer = MusicListSerializer(music_recommend, many=True)
            response_data.append(recommend_serializer.data)
        
        return Response(response_data, status=status.HTTP_200_OK)
    
class MusicDetailView(APIView):
    def get(self, request, music_id):
        serializer_list = []
        music = get_object_or_404(Music, id=music_id)
        serializer = MusicDetailSerializer(music)
        # serializer_list.append(serializer.data)
        # if music in request.user.likes_music.all():
        #     serializer_list.append(1)
        # else:
        #     serializer_list.append(0)
        # reviews = music.review_set.all()
        # review_serializer = ReviewSerializer(reviews,many=True)

        # serializer_list.append(review_serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

        """
        [music],[0,1],[review]

        [music(music,likes,review)]
        """
    

        
class Likeview(APIView):
    def post(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        if request.user in music.likes.all():
            music.likes.remove(request.user)
            return Response("좋아요를 취소했습니다", status=status.HTTP_200_OK)
        else:
            music.likes.add(request.user)
            return Response("좋아요를 눌렀습니다", status=status.HTTP_200_OK)
            
