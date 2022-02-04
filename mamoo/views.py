
from rest_framework import viewsets, permissions
from .models import CustomUser, Mamoo 
from .serializers import  UserSerializer, MamooSerializer
from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response




class UserMamooList(generics.ListAPIView):
    serializer_class = MamooSerializer

    def get_queryset(self):
        user= self.request.user
        return Mamoo.objects.filter(user=user)


class MamooList(viewsets.ModelViewSet):
    queryset = Mamoo.objects.all()
    serializer_class = MamooSerializer
    permission_classes =[permissions.IsAuthenticated]
    

class UserList(viewsets.ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class = UserSerializer




@api_view(['GET'])
def current_user(request):

    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

