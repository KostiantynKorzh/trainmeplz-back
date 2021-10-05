import os

from azure.storage.blob import BlobServiceClient

from app.back.services.storage.imagestorageservice import ImageStorageService
from app.back.services.storage.utils import get_label_from_filename, create_labeled_filename


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
            blob_name = create_labeled_filename(label)
            blob_client = self.blob_service_client.get_blob_client(
                container=label,
                blob=blob_name)
            blob_client.upload_blob(image.read())
        except Exception as e:
            print(str(e))

    def get_filenames_for_all_files_with_label(self, label):
        container = self.blob_service_client.get_container_client(label)
        labeled_filenames = list(map(lambda x: x.name, container.list_blobs()))
        return labeled_filenames

    def delete_all_for_label(self, id):
        pass

    def get_by_filename(self, filename):
        try:
            container_name = get_label_from_filename(filename)
            is_valid_container_name = any(map(str.isdigit, container_name))
            if is_valid_container_name:
                raise Exception('Invalid container name')
            blob = self.blob_service_client.get_blob_client(
                container=container_name,
                blob=filename)
            blob_data = blob.download_blob()
            return blob_data.readall()

        except Exception as e:
            print(str(e))
