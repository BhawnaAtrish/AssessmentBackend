from rest_framework import serializers
from .models import projectData  # Import your model

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectData
        fields = '__all__'  # You can specify the fields you want to include here
