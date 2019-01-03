from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CategoriesViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoriesViewSet)

urlpatterns = router.urls
