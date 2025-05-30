from rest_framework import serializers
from resources.models import Project, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','title','description','type','time_created']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id','project','title','description','assigned_to','priority','issue_type','progress']
    
    def validate_project(self, project):
        """
        Check that the current user is a contributor to the specified project.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if not project.contributors.filter(user=request.user).exists():
                raise serializers.ValidationError(
                    "You must be a contributor to this project to create an issue for it."
                )
        return project

    def validate(self, data):
        """
        Check that the assigned user is a contributor to the specified project.
        """
        assigned_to_user = data.get('assigned_to')
        project = data.get('project')

        if assigned_to_user and project:
            if not project.contributors.filter(pk=assigned_to_user.pk).exists():
                raise serializers.ValidationError(
                    {'assigned_to': "The assigned user must be a contributor to this project."}
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','issue','description','time_created']

    def validate_issue(self, issue):
        """
        Check that the current user is a contributor to the specified project.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if not issue.project.contributors.filter(user=request.user).exists():
                raise serializers.ValidationError(
                    "You must be a contributor to this project to create a comment for it."
                )
        return issue

    