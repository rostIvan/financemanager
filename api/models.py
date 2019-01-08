from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category[name="{self.name}", user_id={self.user_id}, username="{self.user.username}"]'


class Transaction(models.Model):
    category = models.ForeignKey(Category, related_name='transactions', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f""" Transaction[
            user => {self.category.user.username}, category => {self.category.name}, 
            title => {self.title}, amount => {self.amount}, 
            date => {self.datetime}
        ]
        """
