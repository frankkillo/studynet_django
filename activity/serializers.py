from dataclasses import field
from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "course",
            "lesson",
            "created_by",
            "status",
        ]