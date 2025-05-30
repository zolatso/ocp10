from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorModifyContributorReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a resource to edit it.
    To read the resource, you still need to be verified as one of the projects contributors.
    Relationships are different for resources: Project, Issue, Comment
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # Determine the project based on the object type
        project = None
        if hasattr(obj, 'issue'):  # If obj is a Comment instance
            project = obj.issue.project
        if hasattr(obj, 'project'):  # If obj is an Issue instance
            project = obj.project
        elif hasattr(obj, 'contributors'):  # If obj is a Project instance
            project = obj


        user_ids = obj.contributors.values_list('user', flat=True)
        if request.method in SAFE_METHODS:
            return request.user.id in user_ids 

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user