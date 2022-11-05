from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer): 
    music = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = "__all__"