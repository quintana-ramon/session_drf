from rest_framework import serializers
from .models import MyUser

from departments.models import Department


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    def create(self, validated_data):
        instance = MyUser(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            department_id=validated_data["department_id"],
        )
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    def validate_username(self, data):
        users = MyUser.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError("Username already exists!")
        else:
            return data
