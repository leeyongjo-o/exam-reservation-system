from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_admin)


class IsClientUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and not request.user.is_admin)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.pk == request.user.pk
