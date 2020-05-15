from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from rest_framework.viewsets import ModelViewSet

from price_tracker.forms import ProductForm
from price_tracker.models import Product
from price_tracker.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = "price_tracker/product_list.html"
    queryset = Product.objects.filter(name__isnull=False)


class ProductAdd(FormView):
    template_name = "price_tracker/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("product-list")

    def form_valid(self, form):
        form.save()
        return super(ProductAdd, self).form_valid(form)


class ProductDetail(DetailView):
    model = Product
    template_name = "price_tracker/product_detail.html"
