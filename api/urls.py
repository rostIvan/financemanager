from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CategoriesViewSet, username_list, category_list, create_user

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoriesViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('create-user/', create_user),
    path('pretty/usernames/', username_list),
    path('pretty/categories/', category_list)
]
