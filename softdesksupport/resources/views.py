from resources.models import Project
from resources.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework import permissions
from resources.permissions import IsOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


