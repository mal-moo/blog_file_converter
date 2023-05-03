from PIL import ImageOps

from config.config import config
from utils.drawer import Drawer
from utils.image_processor import ImageProcessor


class ImageMaker(ImageProcessor):
    def __init__(self, path, fname):
        super().__init__(path, fname)
        self.path = path
        self.fname = fname
        self.img = self.open_img()
        self.drawer = Drawer()

    def add_border(self, border_size, fill_color):
        border = (border_size, border_size, border_size, border_size)
        self.img = ImageOps.expand(self.img, border=border, fill=fill_color)

    def make_main(self, text):
        self.add_border(10, config.TEXT_BORDER_COLOR)
        self.add_border(60, config.IMAGE_BORDER_COLOR)
        text = '\n'.join(text)
        self.drawer.draw_text_on_image(
            self.img, text, pos_x=105, pos_y=220, font_size=150, rgb=config.TEXT_FILL_COLOR,
            b_rgb=config.TEXT_BORDER_COLOR, spacing=60, stroke_width=8
        )
        return self.img

    def make_beaf(self, text):
        y = 950
        font_size = 70
        self.drawer.draw_text_on_image(
            self.img, text, pos_y=y, font_size=font_size, rgb=config.TEXT_BORDER_COLOR,
            b_rgb=config.IMAGE_BORDER_COLOR, has_background=True
        )
        return self.img

    def make_tel(self, tel_type):
        if tel_type.endswith('1'):
            text = f"클릭하시면 전화로 연결됩니다\n문의 {config.PHONE}"
            y = 850
            font_size = 80
        else:
            text = "클릭하시면\n전화로 연결됩니다"
            y = 800
            font_size = 115
        self.drawer.draw_text_on_image(self.img, text, pos_y=y, font_size=font_size)
        return self.img

    def make_last(self, text):
        y = 700
        font_size = 80
        text = '\n'.join(text)
        self.drawer.draw_text_on_image(
            self.img, text, pos_y=y, font_size=font_size, rgb=config.TEXT_FILL_COLOR,
            b_rgb=config.TEXT_BORDER_COLOR
        )

        y = 950
        font_size = 100
        self.drawer.draw_text_on_image(
            self.img, config.NAME, pos_y=y, font_size=font_size, rgb=config.NAME_FILL_COLOR,
            b_rgb=config.TEXT_FILL_COLOR
        )
        return self.img
