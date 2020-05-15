from urllib.parse import urlparse

from django import forms

from price_tracker.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("product_url",)

    def clean_product_url(self):
        valid_hostname = "fabelio.com"
        product_url = self.cleaned_data["product_url"]
        url = urlparse(product_url)
        if url.hostname != valid_hostname:
            raise forms.ValidationError("Not a product from fabelio")
        return product_url
