from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


USER = "YOUR MONGODB USER"
PASS = "MONGODB ATLAS"
DATABASE = "DB NAME (COLLECTION NAME)"

DEBUG = True

client = MongoClient(f"mongodb+srv://{USER}:{PASS}@cluster0.xper7.mongodb.net/{DATABASE}?ssl=true&ssl_cert_reqs=CERT_NONE")

if DEBUG:
    db = client["test"]
    products = db.products   
else:
    db = client["api-intent"]
    products = db.products   


def saveProductData(product_data):
    product_data["_id"] = product_data["productId"]
    try:
        products.insert_one(product_data)
    except DuplicateKeyError:
        raise Exception("This product already exists!")


def getProductDataByID(product_id):
    product_data = products.find_one({"productId": int(product_id)})
    return product_data


def deleteProductDataByID(product_id):
    product_data = products.delete_one({"productId": int(product_id)})
    
