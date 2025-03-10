from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

class IsMember(BasePermission):
    """
    Allows access only to member users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_member