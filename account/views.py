from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import Profile
from .serializers import UserSerializer, RegisterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        p=Profile(user=user)
        p.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        super(LoginAPI, self).post(request, format=None)
        return Response(
            {
                "user":user.id

            }
        ) 
    


@api_view(['GET', 'POST'])
def profile_data(request):
   
    if request.method == 'POST':
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        user1=request.user
        profile=Profile.objects.get(user=user1)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)
   

