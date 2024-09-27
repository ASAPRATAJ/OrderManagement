from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserCreateView, UserListView, CustomTokenObtainPairView


urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/token/create/', CustomTokenObtainPairView.as_view(), name='token-create'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
