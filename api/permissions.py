from rest_framework import permissions

from users.models import CustomUser


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    (request.user.is_staff or request.user.role == CustomUser.RoleUser.ADMIN)
                    )


class GeneralPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    (request.user.is_staff or
                     request.user.role == CustomUser.RoleUser.ADMIN) or
                    request.method in permissions.SAFE_METHODS)
