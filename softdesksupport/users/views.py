from users.models import User, Contributor
from users.serializers import UserSerializer, ContributorSerializer
from rest_framework import viewsets
#from snippets.permissions import IsOwnerOrReadOnly
##from rest_framework.decorators import api_view, action
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework import renderers

# from rest_framework.response import Response
# from rest_framework import permissions
# from rest_framework import generics

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer