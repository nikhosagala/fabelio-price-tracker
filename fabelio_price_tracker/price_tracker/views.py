from rest_framework.viewsets import ModelViewSet

from price_tracker.models import Product
from price_tracker.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
