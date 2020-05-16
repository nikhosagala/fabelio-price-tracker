from typing import Optional

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel


class FabelioProduct(BaseModel):
    name: str
    unit_price: float
    unit_sale_price: float
    product_image_url: str


def find_product_id(url: str) -> Optional[int]:
    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.content, "html.parser")
    product_id = soup.find(id="productId")
    return product_id.get("value")


def find_product_info_by_id(product_id: int) -> FabelioProduct:
    base_url = "https://fabelio.com/insider/data/product/id"
    resp = requests.get(f"{base_url}/{product_id}")
    product = resp.json().get("product")
    return FabelioProduct(**product)
