from fabelio_price_tracker.app import celery_app
from price_tracker.helpers import find_product_id, find_product_info_by_id
from price_tracker.models import Product


@celery_app.task
def process_product_url():
    products = Product.objects.filter(fabelio_product_id__isnull=True).all()
    for product in products:
        fabelio_product_id = find_product_id(product.product_url)
        fabelio_product = find_product_info_by_id(fabelio_product_id)
        product.name = fabelio_product.name
        product.fabelio_product_id = fabelio_product_id
        product.image_url = fabelio_product.product_image_url
        product.save()
