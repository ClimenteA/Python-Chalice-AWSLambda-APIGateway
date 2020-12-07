import boto3
import uuid
import requests
from io import BytesIO


REGION = "eu-central-1"
BUCKET_NAME = "product-images"

ACCEPTED_IMAGES_FORMAT = ('.jpg','.jpeg','.png','.webp',)


s3 = boto3.client('s3', region_name=REGION)

def listBuckets():
    response = s3.list_buckets()
    return [bucket["Name"] for bucket in response["Buckets"]]


def createBucket(bucket_name):
    buckets = listBuckets()
    if bucket_name not in buckets:
        s3.create_bucket(Bucket=bucket_name, 
        CreateBucketConfiguration={ 'LocationConstraint': REGION })


def downloadImage(url):

    if url.lower().endswith(ACCEPTED_IMAGES_FORMAT):
        r = requests.get(url)
        if r.headers['Content-Type'].startswith("image"):
            return BytesIO(r.content)

    raise Exception(f"Only images of type {ACCEPTED_IMAGES_FORMAT} are accepted!", url)


def uploadFromMediaUrls(image_list):

    s3_image_dict = {}
    for image_url in image_list:

        if not image_url: 
            s3_image_dict[image_url] = "Upload failed!"
            continue
        
        s3_file_path = uuid.uuid4().hex + "-" + image_url.split("/")[-1]
        s3_url = f"https://{BUCKET_NAME}.s3.{REGION}.amazonaws.com/{s3_file_path}" 

        try:
            image_obj = downloadImage(image_url)
        except Exception as e:
            print(str(e))
            s3_image_dict[image_url] = "Upload failed!"
            continue

        s3.upload_fileobj(image_obj, BUCKET_NAME, s3_file_path)
        s3_image_dict[image_url] = s3_url

    #print(s3_image_dict)
    return s3_image_dict
        
