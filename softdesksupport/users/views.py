from users.models import User, Contributor
from users.serializers import UserSerializer, ContributorSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStaffUser

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    Only users with staff status can look at the list of users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]


class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer