from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerModifyContributorReadOnly(BasePermission):
    """
    Custom permission to only allow owners of the project to edit it.
    To read the project, you still need to be verified as one of its contributors.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        user_ids = obj.contributors.values_list('user', flat=True)
        if request.method in SAFE_METHODS:
            return request.user.id in user_ids 

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user