from rest_framework import serializers
from resources.models import Project, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','description','type','time_created']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id',]

    def validate(self, data):
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
        fields = []

    