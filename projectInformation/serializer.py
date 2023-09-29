from rest_framework import serializers
from .models import projectData


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectData
        fields = "__all__"
