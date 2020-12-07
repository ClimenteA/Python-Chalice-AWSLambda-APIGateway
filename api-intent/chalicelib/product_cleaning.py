import re
from .iso_4217 import currencies


def cleanProductName(product_data):  
 
    # Removing brand name
    product_data["productName"] = product_data["productName"].replace(product_data["brand"], "")

    # Remove special characters and clean spaces
    pattern = re.compile(r'[^a-zA-Z0-9\.\s]+')
    product_data["productName"] = re.sub(pattern, '', product_data["productName"]).strip()

    return product_data["productName"]


def cleanProductPrice(product_data):

    # Convert price to float, round to 2 decimals
    price = product_data["price"]["productPrice"]
    price = re.sub(r"[a-zA-Z]", "", price, flags=re.I)
    price = round(float(price), 2)

    # Assign iso4217 correct currency name 
    priceCode = product_data["price"]["productPrice"].split()[-1]
    product_data["price"]["priceCurrency"] = currencies[priceCode]
    
    # Add a new key priceCode and update the processed productPrice
    product_data["price"]["priceCode"] = priceCode
    product_data["price"]["productPrice"] = price

    return product_data["price"]


def cleanProductData(product_data):

    product_data["productName"] = cleanProductName(product_data)
    product_data["price"] = cleanProductPrice(product_data)

    return product_data