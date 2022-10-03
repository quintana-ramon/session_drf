from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "name",
            "last_name",
            "departmentid",
        ]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User(
                username=validated_data["username"],
                email=validated_data["email"],
                name=validated_data["name"],
                last_name=validated_data["last_name"],
                departmentid=validated_data["departmentid"],
            )
            user.set_password(validated_data["password"])
            user.save()
            return user
