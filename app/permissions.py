from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.pk == request.user.pk
