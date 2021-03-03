from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'approved')


