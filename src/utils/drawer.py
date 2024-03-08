import moviepy.editor as mp
from PIL import Image, ImageDraw, ImageFont

from config.config import config


class Drawer:
    def draw_text_on_image(
        self,
        img: Image,
        text: str,
        pos_x: int = None,
        pos_y: int = None,
        font_size: int = 100,
        rgb: list[int] | tuple[int] | str = config.TEXT_FILL_COLOR,
        b_rgb: list[int] | tuple[int] | str = config.TEXT_BORDER_COLOR,
        has_background: bool = False,
        spacing: int = 30,
        stroke_width: int = 4,
        has_rectangle: bool = False
        ) -> Image:
        draw = ImageDraw.Draw(img, 'RGBA')
        font = ImageFont.truetype(str(config.FONT), font_size)

        if has_rectangle:
            draw.rectangle((0, 0, 1200, 400), fill=(255, 255, 255, 170))
        # x, y
        _, _, x, y = draw.textbbox((0, 0), text, font=font)  # x, y = draw.textsize(text, font)
        pos_x = (config.IMG_SIZE-x)/2 if pos_x is None else pos_x
        pos_y = ((config.IMG_SIZE-y)/3) if pos_y is None else pos_y

        # 문자 바탕색
        if has_background:
            bbox = draw.textbbox((pos_x, pos_y), text, font=font, align='center', stroke_width=20)
            draw.rounded_rectangle(bbox, 50, fill=config.TEXT_FILL_COLOR)

        # 문자, 테투리 색상
        rgb = (rgb[0], rgb[1], rgb[2], 50) if isinstance(rgb, list) else rgb
        b_rgb = (b_rgb[0], b_rgb[1], b_rgb[2], 50) if isinstance(b_rgb, list) else b_rgb

        # 문자 삽입
        draw.text(
                (pos_x, pos_y),  # 위치
                text,  # 문구
                font=font,  # 폰트종류, 폰트크기
                fill=rgb,  # 문자색
                stroke_width=stroke_width,  # 테투리 두께
                stroke_fill=b_rgb,  # 테두리 색
                align='center',  # 정렬
                spacing=spacing  # 라인간 공백
            )
        return img

    def draw_text_on_video(self, video, text):
        # 자막 삽입
        textclip = mp.TextClip(
                    text,  # 자막
                    font=config.FONT,  # 폰트종류
                    fontsize=100,  # 폰트 크기
                    color='white',  # 폰트 색상
                    stroke_color='black',  # 테투리 색
                    stroke_width=3  # 테투리 두께
                )

        etime = int(str(video.end).split('.')[0])
        video = video.subclip(0, int(etime))
        sub = textclip.set_pos('bottom').set_duration(etime)

        return mp.CompositeVideoClip([video, sub])
