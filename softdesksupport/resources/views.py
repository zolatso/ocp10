from resources.models import Project
from resources.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from resources.permissions import OwnerModifyContributorReadOnly
from users.models import Contributor


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,
                          OwnerModifyContributorReadOnly]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=project, user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(contributors__user=user)