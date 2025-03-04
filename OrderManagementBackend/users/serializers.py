"""
Serializers for the 'users' app.
Handles data serialization for user registration, authentication, profile management, and listing.
"""

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class EditCustomUserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving and updating user profile data."""
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "company_name",
            "nip",
            "phone_number",
            "invoice_name",
            "company_address",
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer for generating JWT tokens with custom claims using email as login."""
    username_field = "email"  # Tell SimpleJWT to use email instead of username

    def validate(self, attrs):
        """Validate credentials and return token pair."""
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        token["email"] = user.email
        return token


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for creating new users with password validation."""
    class Meta:
        model = CustomUser
        fields = ("id", "email", "company_name", "password", "is_staff", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        """Validate password using Django's built-in validators."""
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        """Create a new user with validated data."""
        return CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            company_name=validated_data.get("company_name", ""),
        )


class ListCustomUserSerializer(serializers.ModelSerializer):
    """Serializer for listing users (admin view)."""
    class Meta:
        model = CustomUser
        fields = ("id", "company_name", "is_staff", "is_superuser")
