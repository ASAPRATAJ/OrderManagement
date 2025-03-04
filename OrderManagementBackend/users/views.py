"""
Views for the 'users' app.
Handles user registration, authentication, profile management, and user listing.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (
    CustomUserSerializer,
    ListCustomUserSerializer,
    CustomTokenObtainPairSerializer,
    EditCustomUserSerializer,
)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Retrieve or update the profile of the currently authenticated user."""
    permission_classes = [IsAuthenticated]
    serializer_class = EditCustomUserSerializer

    def get_object(self):
        """Return the currently logged-in user."""
        return self.request.user


class CustomTokenObtainPairView(TokenObtainPairView):
    """Generate JWT tokens for user authentication."""
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    """Create a new user in the database."""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(generics.ListAPIView):
    """List all users in the database (admin only)."""
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ListCustomUserSerializer
