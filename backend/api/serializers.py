from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """
    class Meta:
        model = User 
        fields = ["id", 'username', 'email', 'role', 'group', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
    """
    Сериализатор для обработки данных входа пользователя.
    Проверяет учетные данные и возвращает объект пользователя при успешной аутентификации.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Неверные учётные данные")


class LogoutSerializer(TokenBlacklistSerializer):
    """
    Сериализатор для logout.
    """
    pass 