from urllib.parse import urlparse

from rest_framework import serializers

from price_tracker.models import Product


class ProductSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_product_url(value):
        valid_hostname = "fabelio.com"
        url = urlparse(value)
        if url.hostname != valid_hostname:
            raise serializers.ValidationError("Not a product from fabelio")
        return value

    class Meta:
        model = Product
        fields = "__all__"
