from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from api.permissions import IsOwner
from api.serializers import UserSerializer, CategorySerializer, AdminCategorySerializer, TransactionSerializer
from api.services import get_users, get_categories, get_transactions


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_users()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('id', 'username', 'email')
    search_fields = ('username', 'email')


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = get_categories()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsOwner)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('id', 'name',)
    search_fields = ('name',)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return get_categories(user=user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminCategorySerializer
        return CategorySerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser))
def username_list(request):
    data = (UserSerializer(u).data['username'] for u in get_users())
    return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsOwner | IsAdminUser))
def category_list(request):
    user = request.user
    if user.is_superuser:
        data = ({'id': u.id,
                 'username': u.username,
                 'categories': serialize_categories_name(u)
                 } for u in get_users())
    else:
        data = serialize_categories_name(user)
    return Response(data)


def serialize_categories_name(user):
    return (CategorySerializer(c).data['name'] for c in get_categories(user=user))


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = get_transactions()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsOwner)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return get_transactions(user=user)
