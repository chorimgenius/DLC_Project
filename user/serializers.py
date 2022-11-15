from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from musics.serializers import MusicSerializer

class UserProfileSerializers(serializers.ModelSerializer):


    followings = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio" , "image", "followings", "followers")

class UserReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("username", "image")

class UserProfileMusicSerializers(serializers.ModelSerializer):
    
    music = MusicSerializer(many=True)

    followings = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio" , "image", "followings", "followers", "music")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    extra_kwargs = {'image': {'required': False}}
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserProfileUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio" , "image")
    extra_kwargs = {'image': {'required': False}}
    
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token