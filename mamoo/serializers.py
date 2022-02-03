from .models import  Mamoo, CustomUser
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    mamoo = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Mamoo.objects.all())
    password = serializers.CharField(write_only=True)


    class Meta:
        model = CustomUser
        fields = ('username', 'mamoo','pk', 'password')


    def create(self, validated_data):
        user = CustomUser.objects.create_user(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user






class MamooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mamoo
        fields = ('title','type','what', 'where', 'user', 'pk')