from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer (serializers.ModelSerializer):

    #profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}



class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #image = serializers.FileField(use_url=False, required=False)
    
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'image')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ( 'username', 'password')
        # extra_kwargs = {'password': {'write_only': True}}


class LogoutSerializer(serializers.Serializer):
    logout = serializers.BooleanField()