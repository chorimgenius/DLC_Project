from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    extra_kwargs = {'image': {'required': False}}
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token