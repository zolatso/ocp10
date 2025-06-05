from rest_framework.permissions import BasePermission

class IsStaffOrOwner(BasePermission):
    def has_permission(self, request, view):
        # Allow staff users to perform any action (including listing all users)
        if request.user and request.user.is_staff:
            return True

        # For non-staff, ensure they are authenticated
        if not (request.user and request.user.is_authenticated):
            return False

        # Prevent non-staff users from listing all users (GET on /users/)
        if request.method == 'GET' and view.action == 'list':
            return False

        # For other actions (retrieve, update, partial_update, destroy) that go to has_object_permission,
        # allow authenticated users to proceed.
        return True

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check. 'obj' here is the User instance being accessed.
        """
        # Staff users can always access any user object
        if request.user and request.user.is_staff:
            return True

        # For non-staff users, they can only access their own user object
        return obj == request.user # Checks if the object's user is the requesting user
    
    
class IsProjectAuthorOrSelfContributor(BasePermission):
    """
    Custom permission to allow:
    - Any authenticated user to create a Contributor (add themselves to a project).
    - Project author to delete a Contributor.
    - Read (GET) is generally not allowed for this ViewSet's list/detail,
      as contributors are viewed via the Project object.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated for any action on this ViewSet
        if not (request.user and request.user.is_authenticated):
            return False

        # Allow POST requests (for creating a Contributor)
        if request.method == 'POST':
            return True

        # For DELETE requests, allow authenticated users to proceed to object-level check
        if request.method == 'DELETE':
            return True

        # Deny all other methods (GET, PUT, PATCH) for this ViewSet
        return False

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check for Contributor instances.
        'obj' here is a Contributor instance.
        """
        # For DELETE requests, only the author of the related project can delete
        if request.method == 'DELETE':
            # Check if the requesting user is the author of the project
            # associated with this Contributor object.
            return obj.project.author == request.user

        # For any other method that somehow reaches here (e.g., if has_permission was less strict),
        # deny by default to align with the "no GET for this ViewSet" requirement.
        return False

