from rest_framework import serializers
from review.models import Review
from user.models import User

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.SerializerMethodField()
    
    def get_review_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("content",)

## User Serializer
class simpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","image",)

class ReviewMusicSerializer(serializers.ModelSerializer):

    user = simpleUserSerializer()

    class Meta:
        model = Review
        fields = "__all__"