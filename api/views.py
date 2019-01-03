from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.permissions import IsOwner
from api.serializers import UserSerializer, CategorySerializer, AdminCategorySerializer
from api.services import get_users, get_categories


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_users()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('username', 'email')
    search_fields = ('username', 'email')


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = get_categories()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsOwner)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('name',)
    search_fields = ('name',)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return get_categories()
        return get_categories(user=user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminCategorySerializer
        return CategorySerializer
