from rest_framework import serializers
from review.models import Review

class ReivewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReivewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("name","content","rank")