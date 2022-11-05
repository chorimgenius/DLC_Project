from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from musics import serializers
from musics.models import Music
from musics.serializers import MusicSerializer, MusicListSerializer
from review.models import Review
from ML_music.Top_100 import Top_100_list
from ML_music.search_music import recommend_music

# Create your views here.
class MusicListView(APIView):
    def get(self, request):
        
        # top10 list
        musics = Top_100_list() # 검색한 음악 리스트
        top10_serializer = MusicListSerializer(musics,many=True)

        # 내 곡 list
        user = self.request.user # User Model
        musics2 = user.likes_music.all()
        my_list_serializer = MusicListSerializer(musics2, many=True)
        
        # 추천 곡 list
        music_recommend = recommend_music(request.user.id) # user_id = request.user.id
        recommend_serializer = MusicListSerializer(music_recommend, many=True)
        
        response_data = []
        response_data.append(top10_serializer.data) # top10
        response_data.append(my_list_serializer.data) # 내 리스트
        response_data.append(recommend_serializer.data) # 추천 곡 리스트
        
        return Response(response_data, status=status.HTTP_200_OK)
    
class MusicDetailView(APIView):
    def get(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        serializer = MusicSerializer(music)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class MusicLikeView(APIView):
    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user in review.likes.all():
            review.likes.remove(request.user)
            return Response("Like Cancellation", status=status.HTTP_200_OK)
        else:
            review.likes.add(request.user)
            return Response("Like Complete", status=status.HTTP_200_OK)
        
        
class Likeview(APIView):
    def post(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        if request.user in music.likes.all():
            music.likes.remove(request.user)
            return Response("좋아요를 취소했습니다", status=status.HTTP_200_OK)
        else:
            music.likes.add(request.user)
            return Response("좋아요를 눌렀습니다", status=status.HTTP_200_OK)
            
            
