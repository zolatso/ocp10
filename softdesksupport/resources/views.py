from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from resources.permissions import AuthorModifyContributorReadOnly
from resources.models import Project, Issue, Comment
from resources.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from users.models import Contributor


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,
                          AuthorModifyContributorReadOnly]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=project, user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(contributors__user=user)
    
    
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated,
                          AuthorModifyContributorReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Issue.objects.all()
        return Issue.objects.filter(project__contributors__user=user)
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,
                          AuthorModifyContributorReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(issue__project__contributors__user=user)
