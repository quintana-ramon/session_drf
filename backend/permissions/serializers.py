from rest_framework import serializers

from .models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["productid", "departmentid", "permissions"]

        def create(self, validated_data):

            permission = Permission(
                productid=validated_data["productid"],
                departmentid=validated_data["departmentid"],
                permissions=validated_data["permissions"],
            )
            permission.save()
            return permission
