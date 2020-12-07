# https://requests.readthedocs.io/en/master/
# https://github.com/assertpy/assertpy

import json
import pytest
import requests
from assertpy import assert_that


TEST_LOCAL = True


if TEST_LOCAL:
    API_URL = "http://localhost:8000"
else:
    API_URL = "https://asdasdasdasd.execute-api.eu-central-1.amazonaws.com/api"


RETAILER_URL="https://raw.githubusercontent.com/ClimenteA/Python-Chalice-AWSLambda-APIGateway/main/retailer-data.json"


# Delete test product at first
# http localhost:8000/products/42/delete 
def test_product_delete_by_id():
    response = requests.get(API_URL + "/products/42/delete")
    assert_that(response.json()).contains_entry({"message": "Product deleted!"})


# http localhost:8000
def test_index_get_route():
    response = requests.get(API_URL)
    assert_that(response.json()).is_equal_to({'hello': 'world!'})


# http POST localhost:8000/products URL="https://raw.githubusercontent.com/ClimenteA/Python-Chalice-AWSLambda-APIGateway/main/retailer-data.json"
def test_product_post_from_retailer_url():
    products_url = API_URL + "/products"
    response = requests.post(products_url, json={"URL":RETAILER_URL})
    assert_that(response.json()).contains_entry({"message": "Success!"})


# http POST localhost:8000/products URL="https://raw.githubusercontent.com/ClimenteA/Python-Chalice-AWSLambda-APIGateway/main/retailer-data.json"
def test_product_post_from_retailer_url_fail_overwrite():
    products_url = API_URL + "/products"
    response = requests.post(products_url, json={"URL":RETAILER_URL})
    assert_that(response.json()).contains_entry({"message": "This product already exists!"})


# http localhost:8000/products/42
def test_product_get_by_id():
    response = requests.get(API_URL + "/products/42")
    assert_that(response.json()).contains_entry({'productId': 42})


# http localhost:8000/products/42/delete 
def test_product_delete_by_id():
    response = requests.get(API_URL + "/products/42/delete")
    assert_that(response.json()).contains_entry({"message": "Product deleted!"})


