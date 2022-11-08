from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserSerializer, UserProfileSerializers, UserProfileUpdateSerializers, CustomObtainPairSerializer, UserProfileMusicSerializers
from django.shortcuts import get_object_or_404
from musics.serializers import MusicListSerializer

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("Unfollow 했습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("follow 했습니다.", status=status.HTTP_200_OK)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
    
class ProfileView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer_list = []
        musics = User.objects.get(id=user_id).likes_music.all()
        music_serializer = MusicListSerializer(musics,many=True)
        serializer_user = UserProfileSerializers(user)
        serializer_list.append(serializer_user.data)
        serializer_list.append(music_serializer.data)
        return Response(serializer_list, status=status.HTTP_200_OK)
    
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileUpdateSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)