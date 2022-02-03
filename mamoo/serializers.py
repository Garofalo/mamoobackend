from .models import  Mamoo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    mamoo = serializers.StringRelatedField(many=True)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('username', 'password', 'mamoo')


# class ProfileSerializer(serializers.ModelSerializer):
#     mamoo = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Profile
#         fields = ('pk', 'mamoo',)


class MamooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mamoo
        fields = ('title','type','what', 'where', 'user')
