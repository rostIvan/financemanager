from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'password')


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.create(user=user, **validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user')
