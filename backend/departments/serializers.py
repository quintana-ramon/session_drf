from dataclasses import field
from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name"]

        def create(self, validated_data):
            department = Department(name=validated_data["name"])
            department.save()
            return department
