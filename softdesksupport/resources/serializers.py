from rest_framework import serializers
from resources.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','title','description','type','author','time_created']