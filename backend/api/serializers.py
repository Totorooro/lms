from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id", 'username', 'email', 'role', 'group', 'direction', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Неверные учётные данные")
