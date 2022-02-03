
from rest_framework import viewsets, permissions
from .models import Mamoo 
from .serializers import  UserSerializer, MamooSerializer, UserSerializerWithToken
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

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)