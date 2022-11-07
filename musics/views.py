from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filter import SearchFilter
from musics import serializers
from musics.models import Music
from musics.serializers import MusicSerializer
# from ML_music.music_rc import recommend_songs
from review.models import Review

# Create your views here.
class MusicListView(APIView):
    def get(self, request):
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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

class Search(APIView):
    def post(self, request):
        data=request.data
        mu