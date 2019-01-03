from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'date_joined', 'password')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'user')
