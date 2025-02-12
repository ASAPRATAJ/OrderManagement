from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (CustomUserSerializer,
                          ListCustomUserSerializer,
                          CustomTokenObtainPairSerializer,
                          EditCustomUserSerializer)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EditCustomUserSerializer

    def get_object(self):
        return self.request.user  # Zwróć aktualnie zalogowanego użytkownika

class UserEditView(generics.UpdateAPIView):
    """View for editing user profile in database."""
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EditCustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """View for creating JWT token, to be able to authorize user."""
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    """View for creating new user in database."""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(generics.ListAPIView):
    """View for listing users from database."""
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ListCustomUserSerializer
