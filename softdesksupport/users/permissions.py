from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        # Only allow access if the user is authenticated and is staff
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
