from .models import  Mamoo
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


# class UserSerializer(serializers.ModelSerializer):
    
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

#     class Meta:
#         model = User
#         fields = ('username', 'mamoo','pk')


# class ProfileSerializer(serializers.ModelSerializer):
#     mamoo = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Profile
#         fields = ('pk', 'mamoo',)


class MamooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mamoo
        fields = ('title','type','what', 'where', 'user')



class UserSerializer(serializers.ModelSerializer):

    mamoo = serializers.StringRelatedField(many=True, required=False)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'mamoo', 'pk')


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    mamoo = serializers.StringRelatedField(many=True, required=False)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'mamoo')