from django.test import TestCase
from .models import Category, User
from .services import get_users, get_user, get_categories


class CategoriesTestCase(TestCase):
    def setUp(self):
        User.objects.create(pk=1, username='john', email='john@gmail.com')
        User.objects.create(pk=2, username='alex', email='alex@gmail.com')
        Category.objects.create(name='Food', user_id=1)
        Category.objects.create(name='Beer', user_id=1)
        Category.objects.create(name='Clothes', user_id=2)
        Category.objects.create(name='Rent', user_id=2)

    def test_user_objects_saving(self):
        john = get_user(pk=1)
        alex = get_user(pk=2)
        users = get_users()
        self.assertEqual(john.username, 'john')
        self.assertEqual(alex.username, 'alex')
        self.assertEqual(john.email, 'john@gmail.com')
        self.assertEqual(alex.email, 'alex@gmail.com')
        self.assertEqual(len(users), 2)
        self.assertSetEqual(set(u.username for u in users), {'john', 'alex'})

    def test_category_objects_saving(self):
        categories = get_categories()
        self.assertEqual(len(categories), 4)
        john_categories = get_categories(user_id=1)
        alex_categories = get_categories(user_id=2)
        self.assertEqual(len(john_categories), 2)
        self.assertEqual(len(alex_categories), 2)
        self.assertSetEqual(set(c.name for c in john_categories), {'Food', 'Beer'})
        self.assertSetEqual(set(c.name for c in alex_categories), {'Clothes', 'Rent'})

