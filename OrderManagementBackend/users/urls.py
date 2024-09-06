from django.urls import path
from .views import UserCreateView, UserListView

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
]
