from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'company_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                company_name=validated_data.get('company_name', ''),
            )
            return user
        except ValueError as e:
            # Tutaj przechwytujemy błąd ValueError i zwracamy go jako ValidationError
            raise serializers.ValidationError({'detail': str(e)})


class ListCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'company_name')

