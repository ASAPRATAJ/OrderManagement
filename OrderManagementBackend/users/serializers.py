from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError

from .models import CustomUser


class EditCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'company_name', 'password', 'nip', 'phone_number',
                  'invoice_name', 'company_address')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): # noqa
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        return token


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'company_name', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Walidacja hasła przy użyciu globalnych walidatorów Django.
        """
        try:
            validate_password(value)  # Wywołanie globalnych walidatorów haseł
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)  # Przekazanie błędów do DRF
        return value

    def create(self, validated_data):
        """
        Tworzenie użytkownika z walidacją danych.
        """
        company_name = validated_data.get('company_name', '')
        email = validated_data['email']
        password = validated_data['password']

        try:
            # Użycie metody create_user z modelu CustomUser
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                company_name=company_name,
            )
            return user
        except Exception as e:
            # Obsługa błędów podczas tworzenia użytkownika
            raise serializers.ValidationError({'detail': str(e)})


class ListCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'company_name', 'is_staff', 'is_superuser')
