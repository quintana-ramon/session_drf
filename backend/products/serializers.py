from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]

        def create(self, validated_data):
            product = Product(
                name=validated_data["name"],
                amount=validated_data["amount"],
                description=validated_data["description"],
            )
            product.save()
            return product
