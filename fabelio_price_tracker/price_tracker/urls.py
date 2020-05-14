from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from price_tracker.views import ProductViewSet

router = routers.SimpleRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    url("", include(router.urls)),
]
