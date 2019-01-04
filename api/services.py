from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print(f'user `{instance}` made token => {token}`')


def create_tokens():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
