from PIL import Image

from config.config import config


class ImageProcessor:
    def __init__(self, path: str, filename: str):
        self.filename = filename
        self.image_path = path + filename

    def open_img(self) -> Image:
        try:
            img = Image.open(self.image_path)
        except FileNotFoundError:
            extension = self.filename.split('.')[-1]
            if extension == 'jpg':
                img = Image.open(self.image_path.replace('jpg', 'jpeg'))
        except Exception as e:
            print(e)

        img = img.resize((config.IMG_SIZE, config.IMG_SIZE), Image.LANCZOS)

        return img
