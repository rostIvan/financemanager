from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category, Transaction


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.create(user=user, name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AdminCategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Category
        fields = ('id', 'name', 'username', 'user')


class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    category_name = serializers.CharField(source='category.name', allow_null=True)

    class Meta:
        model = Transaction
        fields = ('id', 'category_name', 'title', 'description', 'amount', 'datetime')

    def create(self, validated_data):
        user = self.context['request'].user
        category = Category.objects.get_or_create(user=user, name=validated_data['category']['name'])[0]
        transaction = Transaction.objects.create(category=category,
                                                 title=validated_data['title'],
                                                 description=validated_data.get('description', ''),
                                                 amount=validated_data['amount'],
                                                 datetime=validated_data.get('datetime', None))
        return transaction

    def update(self, instance, validated_data):
        user = self.context['request'].user
        update_category(instance, user, validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance


def update_category(instance, user, validated_data):
    category_name = validated_data.get('category').get('name') \
        if validated_data.get('category') and validated_data.get('category').get('name') else None
    if category_name:
        category = Category.objects.get_or_create(user=user, name=category_name)[0]
        instance.category = category or instance.category


class BasicTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'title', 'description', 'amount', 'datetime')


class PrettyTransactionsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='name')
    transactions = BasicTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('category', 'transactions')
