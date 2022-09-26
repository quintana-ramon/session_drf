from rest_framework import serializers

from .models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    save = serializers.BooleanField(required=False)
    read = serializers.BooleanField(required=False)
    update = serializers.BooleanField(required=False)
    delete = serializers.BooleanField(required=False)

    def validate_save(self, value):
        print(type(value))
        return value

    class Meta:
        model = Permission
        fields = ["save", "read", "update", "delete", "departmentid"]

        def create(self, validated_data):

            permission = Permission(
                save=validated_data["save"],
                read=validated_data["read"],
                update=validated_data["update"],
                delete=validated_data["delete"],
                departmentid=validated_data["departmentid"],
            )
            permission.save()
            return permission
