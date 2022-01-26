from .models import Profile, Mamoo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    mamoos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'mamoos')


class MamooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mamoo
        fields = '__all__'
