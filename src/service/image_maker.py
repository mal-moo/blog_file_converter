from PIL import Image, ImageOps

from config.config import config
from utils.drawer import Drawer


class ImageMaker:
    def __init__(self, drawer: Drawer):
        self.path = None
        self.fname = None
        self.img = None
        self.drawer = drawer

    def setter(self, path: str, filename: str):
        self.path = path
        self.fname = filename

    def _add_border(self, border_size: int, fill_color: tuple[int]) -> None:
        border = (border_size, border_size, border_size, border_size)
        self.img = ImageOps.expand(self.img, border=border, fill=fill_color)

    def open_img(self) -> Image:
        image_path = self.path + self.fname
        try:
            img = Image.open(image_path)
        except FileNotFoundError:
            extension = self.filename.split('.')[-1]
            if extension == 'jpg':
                img = Image.open(image_path.replace('jpg', 'jpeg'))
        except Exception as e:
            print(e)

        self.img = img.resize((config.IMG_SIZE, config.IMG_SIZE), Image.LANCZOS)

    def make_main(self, text: str) -> Image:
        # self._add_border(8, config.TEXT_BORDER_COLOR)
        self._add_border(50, config.IMAGE_BORDER_COLOR)

        # text = '\n'.join(text)
        # self.drawer.draw_text_on_image(
        #     self.img, text, pos_x=config.MAIN_POSITION_X, pos_y=config.MAIN_POSITION_Y, font_size=config.MAIN_FONT_SIZE, rgb=config.TEXT_FILL_COLOR,
        #     b_rgb=config.TEXT_BORDER_COLOR, spacing=70, stroke_width=7
        # )
        return self.img

    def make_beaf(self, text: str) -> Image:
        y = 950
        font_size = 70
        self.drawer.draw_text_on_image(
            self.img, text, pos_y=y, font_size=font_size, rgb=config.TEXT_BORDER_COLOR,
            b_rgb=config.IMAGE_BORDER_COLOR, has_background=True
        )
        return self.img

    def make_tel(self, tel_type: str) -> Image:
        if tel_type.endswith('1'):
            text = f"리페어브라더스\n클릭시 전화연결됩니다."
            y = 850
            font_size = 80
        else:
            text = "사진 클릭시 전화연결됩니다."
            y = 930
            font_size = 90
        self.drawer.draw_text_on_image(self.img, text, pos_y=y, font_size=font_size, rgb=config.TEXT_BORDER_COLOR,
            b_rgb=config.TEXT_FILL_COLOR)
        return self.img

    def make_last(self, text: str) -> Image:
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
