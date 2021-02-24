from rest_framework import permissions

from users.models import User


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and (
                request.user.is_superuser or
                request.user.role == User.RoleUser.ADMIN))


class GeneralPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and (
                request.user.is_staff or
                request.user.role == User.RoleUser.ADMIN) or
            request.method in permissions.SAFE_METHODS)


class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and User.objects.filter(email=user))


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser == 1 or
                request.user.role == 'admin')
