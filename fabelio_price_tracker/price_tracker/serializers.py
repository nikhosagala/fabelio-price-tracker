from rest_framework.serializers import ModelSerializer

from price_tracker.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
