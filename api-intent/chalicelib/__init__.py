from .product_schema import productSchemaIsValid
from .product_cleaning import  cleanProductData
from .s3_buckets import createBucket, BUCKET_NAME
from .s3_buckets import uploadFromMediaUrls
from .mongodb_atlas import (
    saveProductData, 
    getProductDataByID, 
    deleteProductDataByID
)

# Create bucket if not found 
# (commented because bucket is created)
# createBucket(BUCKET_NAME)
