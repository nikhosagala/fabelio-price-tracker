from collections import namedtuple
from typing import Optional

import requests
from bs4 import BeautifulSoup


class Product(
    namedtuple("Product", "name unit_price unit_sale_price url product_image_url")
):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        for key in tuple(kwargs):
            if key not in cls._fields:
                del kwargs[key]
        return super().__new__(cls, *args, **kwargs)


def find_product_id(url: str) -> Optional[int]:
    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.content, "html.parser")
    product_id = soup.find(id="productId")
    return product_id.get("value")


def find_product_info_by_id(product_id: int) -> Product:
    base_url = "https://fabelio.com/insider/data/product/id"
    resp = requests.get(f"{base_url}/{product_id}")
    product = resp.json().get("product")
    return Product(**product)
