import os

from azure.storage.blob import BlobServiceClient

from src.back.services.storage.imagestorageservice import ImageStorageService
from src.back.services.storage.utils import get_label_from_filename, create_labeled_filename
from src.back.setup import logger


class AzureBlobImageStorageService(ImageStorageService):

    def __init__(self):
        super().__init__()
        self.conn_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        self.blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)

    def save(self, image, label):
        try:
            container_client = self.blob_service_client.get_container_client(label)
            if not container_client.exists():
                logger.info('Creating new container in Azure Storage for label: {}'.format(label))
                container_client.create_container()
            blob_name = create_labeled_filename(label)
            blob_client = self.blob_service_client.get_blob_client(
                container=label,
                blob=blob_name)
            blob_client.upload_blob(image.read())
            logger.debug('Uploading blob with label: {}'.format(label))
        except Exception:
            logger.exception('Error uploading blob with label: {}'.format(label))

    def get_filenames_for_all_files_with_label(self, label):
        container = self.blob_service_client.get_container_client(label)
        labeled_filenames = list(map(lambda x: x.name, container.list_blobs()))
        logger.debug('Getting filenames for all files with label: {}'.format(label))
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
            logger.debug('Getting file from Azure Storage by filename: {}'.format(filename))
            return blob_data.readall()

        except Exception:
            logger.exception('Error getting blob with filename: {}'.format(filename))
