from resources.models import Project
from resources.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework import permissions
from resources.permissions import IsOwnerOrReadOnly
from users.models import Contributor


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=project, user=self.request.user)