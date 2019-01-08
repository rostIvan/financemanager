from rest_framework import permissions

from api.models import Transaction


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Transaction):
            return obj.category.user == request.user
        return obj.user == request.user
