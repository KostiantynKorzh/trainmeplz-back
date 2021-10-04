from app.back.db import imagestorageservice


def save_image(image, label):
    imagestorageservice.save(image, label)
