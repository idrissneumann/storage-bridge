import os

from minio import Minio
from utils.common import is_disabled

BUCKET_URL = os.getenv('BUCKET_URL')
BUCKET_REGION = os.getenv('BUCKET_REGION')
BUCKET_ACCESS_KEY = os.getenv('BUCKET_ACCESS_KEY')
BUCKET_SECRET_KEY = os.getenv('BUCKET_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
BUCKET_FOLDER = os.getenv('BUCKET_FOLDER')

minioClient = None

if not any(is_disabled(setting) for setting in [BUCKET_URL, BUCKET_REGION, BUCKET_ACCESS_KEY, BUCKET_SECRET_KEY, BUCKET_NAME]):
    minioClient = Minio(BUCKET_URL,
                    region=BUCKET_REGION,
                    access_key=BUCKET_ACCESS_KEY,
                    secret_key=BUCKET_SECRET_KEY)

def get_minio_client():
    return minioClient

def get_bucket_name():
    return BUCKET_NAME

def get_bucket_folder():
    if is_disabled(BUCKET_FOLDER):
        return "/"

    return "{}/".format(BUCKET_FOLDER)