class ImageRepo:

    def __init__(self, db, grid_fs):
        self.db = db
        self.grid_fs = grid_fs

    def save_image(self, label, data):

        print(data)
        print(''.join(map(str, data)))
        print(int(''.join(map(str, data)), 2))
        print(bin(int(''.join(map(str, data)), 2) << 1))

        a = self.grid_fs.put(bin(int(''.join(map(str, data)), 2) << 1), encoding='utf-8', label='cat')
        print(self.grid_fs.get(a).read())

    def get_all_images_for_label(self, label):
        return self.db.model.find_one({'label': label})['images']
