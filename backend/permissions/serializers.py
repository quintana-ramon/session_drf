from rest_framework import serializers

from .models import AdminUser, FinanceUser, PurchasingUser, SalesUser


class AdminUserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = AdminUser
        fields = ["username", "email", "password", "name", "last_name", "type"]
        extra_kwargs = {"password": {"write_only": True}}

    def get_type(self, obj):
        pass

        def create(self, validated_data):
            if validated_data["type"]:
                print("success")
            user = AdminUser(
                username=validated_data["username"],
                email=validated_data["email"],
                name=validated_data["name"],
                last_name=validated_data["last_name"],
            )
            user.set_password(validated_data["password"])
            user.save()
            return user
