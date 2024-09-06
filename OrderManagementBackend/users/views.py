from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer, ListCustomUserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListCustomUserSerializer
