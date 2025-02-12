from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserCreateView, UserListView, CustomTokenObtainPairView, UserEditView, UserProfileView


urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/token/create/', CustomTokenObtainPairView.as_view(), name='token-create'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/profile/', UserProfileView.as_view(), name='user-profile'),
    path('users/profile/edit/', UserEditView.as_view(), name='user-edit'),
]
