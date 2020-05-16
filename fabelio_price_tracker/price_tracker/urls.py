from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from price_tracker.views import (ProductAdd, ProductDetail, ProductListView,
                                 ProductViewSet)

router = routers.SimpleRouter()
router.register("products", ProductViewSet, basename="api-product")

urlpatterns = [
    url("", include(router.urls)),
    path("product-list", ProductListView.as_view(), name="product-list"),
    path("product-add", ProductAdd.as_view(), name="product-add"),
    path("product-detail/<int:pk>", ProductDetail.as_view(), name="product-detail"),
]
