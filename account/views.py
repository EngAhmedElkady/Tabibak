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
    


@api_view(['GET','PUT'])
def profile_data(request):

    if request.method == 'PUT':
        user1=request.user
        profile=Profile.objects.get(user=user1)
        profile.phone=request.data['phone']
        # profile.photo=request.data['photo']
        profile.save()
        return Response({
            "phone":profile.phone,
            "photo":str(profile.photo),
        })

    else:
        user1=request.user
        profile=Profile.objects.get(user=user1)
        data1={}
        data1["username"]=user1.username
        data1["email"]=user1.email
        data1["phone"]=profile.phone
        data1["photo"]=profile.photo
        return Response({
            "username":user1.username,
            "email":user1.email,
            "phone":profile.phone,
            "photo":str(profile.photo),
        })


