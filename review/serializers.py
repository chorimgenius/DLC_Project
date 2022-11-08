from rest_framework import serializers
from review.models import Review
from user.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.SerializerMethodField()
    
    def get_review_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
    review_user = serializers.SerializerMethodField()
    
    def get_review_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = ("content","review_user",)