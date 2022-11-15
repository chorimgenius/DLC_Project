from rest_framework import serializers
from musics.models import Music
from review.serializers import ReviewMusicSerializer
from user.models import User

class MusicListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Music
        fields = "__all__"
        
class MusicSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Music
        fields = "__all__"


## 임시
class MusicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class MusicDetailSerializer(serializers.ModelSerializer): 

    review_set = ReviewMusicSerializer(many=True)
    likes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Music
        fields = '__all__'

