from app.back.application import imagestorageservice


def save_image(image, label):
    imagestorageservice.save(image, label)
