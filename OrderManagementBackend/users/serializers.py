from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        return token


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'company_name', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Rozdzielenie logiki biznesowej od tworzenia użytkownika
        company_name = validated_data.get('company_name', '')
        email = validated_data['email']
        password = validated_data['password']

        # Obsługa potencjalnych błędów w tworzeniu użytkownika
        try:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                company_name=company_name,
            )
            return user
        except ValueError as e:
            raise serializers.ValidationError({'detail': str(e)})


class ListCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'company_name', 'is_staff', 'is_superuser')
