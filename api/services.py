from django.contrib.auth.models import User
from django.db.models import QuerySet
from .models import Category


def get_users() -> QuerySet:
    return User.objects.all().order_by('date_joined')


def get_user(pk) -> User:
    return User.objects.get(pk=pk)


def get_categories(user=None, user_id=None) -> QuerySet:
    if user:
        return Category.objects.filter(user=user)
    elif user_id:
        return Category.objects.filter(user_id=user_id)
    return Category.objects.all()
