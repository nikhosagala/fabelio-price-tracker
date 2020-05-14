from django.db import models

from price_tracker.mixins import BaseModelMixin


class Product(BaseModelMixin):
    product_url = models.URLField(unique=True)
    fabelio_product_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "products"
        ordering = ["-created"]


class ProductPrice(BaseModelMixin):
    unit_price = models.IntegerField(default=0)
    unit_sale_price = models.IntegerField(default=0)

    class Meta:
        db_table = "product_prices"
