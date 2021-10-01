import os
import uuid

from azure.storage.blob import BlobServiceClient, ContainerClient

from app.back.services.storage.imagestorageservice import ImageStorageService


class AzureBlobImageStorageService(ImageStorageService):

    def __init__(self):
        self.conn_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        self.blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)

    def save(self, image, label):
        try:
            container_client = self.blob_service_client.get_container_client(label)
            if not container_client.exists():
                print("Creating container")
                container_client.create_container()
            blob_client = self.blob_service_client.get_blob_client(container=label, blob=str(uuid.uuid4()))
            blob_client.upload_blob(image.read())
        except Exception as e:
            print(str(e))

    def get_all_for_label(self, label):
        return super().get_all_for_label(label)

    def delete_all_for_label(self, id):
        return super().delete(id)
