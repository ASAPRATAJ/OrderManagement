from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomUser
from .serializers import CustomUserSerializer, ListCustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ListCustomUserSerializer
