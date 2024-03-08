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
        text = '\n'.join(text)
        self.drawer.draw_text_on_image(
            self.img, text, pos_x=config.MAIN_POSITION_X, pos_y=config.MAIN_POSITION_Y, font_size=config.MAIN_FONT_SIZE, rgb=config.NAME_FILL_COLOR,
            stroke_width=0, has_rectangle=True
        )
        self._add_border(50, config.IMAGE_BORDER_COLOR)

        return self.img

    def make_beaf(self, text: str) -> Image:
        x = 10
        y = 10
        font_size = 140
        self.drawer.draw_text_on_image(
            self.img, text, pos_x=x, pos_y=y, font_size=font_size, rgb=config.TEXT_BORDER_COLOR,
            stroke_width=0
        )
        return self.img

    def make_tel(self, tel_type: str) -> Image:
        if tel_type.endswith('1'):
            text = f"문의방법\n사진클릭\n전화연결"
            y = 250
            font_size = 180
        else:
            text = "사진 누르면 전화\n상담 연결 됩니다"
            y = 700
            font_size = 120
        self.drawer.draw_text_on_image(self.img, text, pos_y=y, font_size=font_size, rgb=config.NAME_FILL_COLOR, b_rgb=config.NAME_FILL_COLOR, spacing=50, stroke_width=0)
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
