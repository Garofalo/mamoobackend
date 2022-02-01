from .models import Profile, Mamoo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    mamoo = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        
        fields = ('user','mamoo')


class MamooSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mamoo
        fields = '__all__'
