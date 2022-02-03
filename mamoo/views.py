
from rest_framework import viewsets, permissions
from .models import Mamoo 
from .serializers import  UserSerializer, MamooSerializer
from django.contrib.auth.models import User



class MamooList(viewsets.ModelViewSet):
    queryset = Mamoo.objects.all()
    serializer_class = MamooSerializer
    permission_classes =[permissions.IsAuthenticated]
    
# class ProfileList(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes =[permissions.IsAuthenticatedOrReadOnly]

class UserList(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer