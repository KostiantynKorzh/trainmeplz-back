import os

from src.back.setup import dataset_db

image_storage_approach = os.getenv('IMAGE_STORAGE_APPROACH')

from src.back.services.storage.azureblobimagestorageservice import AzureBlobImageStorageService
from src.back.services.storage.mongoimagestorageservice import MongoImageStorageService

if image_storage_approach == 'blob':
    imagestorageservice = AzureBlobImageStorageService()
else:
    imagestorageservice = MongoImageStorageService(dataset_db)