from rest_framework import serializers
from .models import ProjectAPI

class ProjectAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAPI
        fields = ('id', 'name', 'project_link', 'repository_link')