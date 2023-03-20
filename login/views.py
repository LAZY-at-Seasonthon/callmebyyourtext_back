from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer, LoginSerializer #, MyTokenObtainPairSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
                               # all methods need Authenticate  # => GET method 허용시 사용
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout
from rest_framework.views import APIView

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileList(generics.RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = ProfileSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request): 
        user = User.objects.get(email=request.data['email'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        login(request, user)
        return Response({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'token': token.key,},
            status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    def get(self, request, format=None):
        # using Django logout
        logout(request)
        return Response(status=status.HTTP_200_OK)