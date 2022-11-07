from rest_framework import serializers
from musics.models import Music

class MusicListSerializer(serializers.ModelSerializer): 
    # music = serializers.SerializerMethodField()
    
    class Meta:
        model = Music
        fields = "__all__"
        
class MusicSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Music
        fields = "__all__"
