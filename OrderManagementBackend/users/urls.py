"""
URL configuration for the 'users' app.
Handles user registration, authentication, and profile management.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserCreateView,
    UserListView,
    CustomTokenObtainPairView,
    UserProfileView,
)

urlpatterns = [
    # User management
    path("", UserListView.as_view(), name="user-list"),  # GET: List users
    path("register/", UserCreateView.as_view(), name="user-register"),  # POST: Create user

    # Authentication
    path("login/", CustomTokenObtainPairView.as_view(), name="token-obtain"),  # POST: Get JWT
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),  # POST: Refresh JWT

    # Profile management
    path("profile/", UserProfileView.as_view(), name="user-profile"),  # GET/PUT/PATCH: View profile
]
