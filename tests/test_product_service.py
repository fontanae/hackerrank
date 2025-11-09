import os
import json
from service.productService import ProductService

def test_get_all_products_without_filters():
    service = ProductService()
    products = service.get_all_products()

    assert isinstance(products,list)
    assert len(products)>0
    assert "description" not in products[0]

def test_products_with_name_filter():
    service = ProductService()
    products = service.get_all_products(name="mouse")

    assert isinstance(products,list)
    assert len(products)>0
    assert all("mouse" in p["name"].lower() for p in products)

def test_products_with_price_filter():
    service = ProductService()
    products = service.get_all_products(min_price=40000)

    assert isinstance(products,list)
    assert len(products)>0
    assert all(float(p["value"])>=40000 for p in products)

def test_get_one_product_found():
    service = ProductService(local=True)
    product = service.get_one_product("P001")

    assert isinstance(product, dict)
    assert product["id"]=="P001"

def test_get_one_product_not_found():
    service = ProductService(local=True)
    product = service.get_one_product("INVALID-ID")

    assert isinstance (product,dict)
    assert "error" in product