import requests
from chalice import Chalice

from chalicelib import (
    productSchemaIsValid,
    cleanProductData,
    uploadFromMediaUrls,
    saveProductData,
    getProductDataByID,
    deleteProductDataByID
)


app = Chalice(app_name='api-intent')

# All commented lines are for debugging
# app.debug = False


# http localhost:8000
@app.route('/')
def index():
    return {'hello': 'world!'}


# http POST localhost:8000/products
# http POST localhost:8000/products URL="https://bad-url.nogood"

# image_list = [
#     "https://softgata.com/assets/django.png",
#     "https://softgata.com/assets/fastapi.svg",
#     "https://softgata.com/assets/svelte.svg"
# ]

@app.route('/products', methods=['POST'])
def saveProduct():

    payload = app.current_request.json_body

    if not payload: 
        return { "message": "URL not found!", "productData": None }

    if 'URL' in payload:
        try:
            product_data = requests.get(payload["URL"]).json()
        except:
            return { "message": "Invalid URL!", "productData": None }
            
        #product_data = {"bad": "productData"}
        if not productSchemaIsValid(product_data):
            return { "message": "Invalid product schema!", "productData": None }
        
        product_data = cleanProductData(product_data)
        product_data["media"]["uploadedImages"] = uploadFromMediaUrls(product_data["media"]["images"])
        #product_data["media"]["uploadedImages"] = uploadFromMediaUrls(image_list)
        
        try:
            saveProductData(product_data)
        except Exception as e:
            return { "message": str(e), "productData": None } 
    
        return { "message": "Success!", "productData": product_data }  
            

# http localhost:8000/products/42 
@app.route('/products/{productId}', methods=['GET'])
def getProduct(productId):
    try:
        product_data = getProductDataByID(productId)
        if not product_data: return {"message": "Product not found!"} 
        return { "message": "Success!", "productData": product_data }
    except:#if not int
        return {"message": "Missing ID!", "productData": None}

        
# http localhost:8000/products/
@app.route('/products', methods=['GET'])
def failProduct():
    return {"message": "Missing ID!", "productData": None}


# http localhost:8000/products/42/delete 
@app.route('/products/{productId}/delete', methods=['GET'])
def deleteProduct(productId):
    try:
        deleteProductDataByID(productId)
        return {"message": "Product deleted!"}
    except:
        return {"message": "Missing ID!"}
    
