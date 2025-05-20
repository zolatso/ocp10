from resources.models import Project
from resources.serializers import ProjectSerializer
from rest_framework import viewsets
#from snippets.permissions import IsOwnerOrReadOnly
##from rest_framework.decorators import api_view, action
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework import renderers

# from rest_framework.response import Response
# from rest_framework import permissions
# from rest_framework import generics


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


