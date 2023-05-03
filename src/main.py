# brew install imagemagick or brew update && brew install imagemagick
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
import os
import sys
from pathlib import Path

from config.config import config
from const.enum import TYPE_FILE_NUMBER, TYPE_IMAGE
from service.image_maker import ImageMaker
from service.video_maker import VideoMaker
from utils.location import Location


def file_maker(path: str, filename: str) -> str | None:
    img = None
    f, extension = os.path.splitext(filename)

    match f:
        case TYPE_FILE_NUMBER.ONE:
            img = ImageMaker(path, fname).make_main(config.TITLE)
            dname = 'fin_main.jpg'
        case TYPE_FILE_NUMBER.TWO | TYPE_FILE_NUMBER.THREE:
            text = '시공전' if f == '2' else '시공후'
            img = ImageMaker(path, fname).make_beaf(text)
            dname = f'fin_{text}.jpg'
        case TYPE_FILE_NUMBER.FOUR | TYPE_FILE_NUMBER.FIVE:
            itype = '1' if f == '4' else '2'
            img = ImageMaker(path, fname).make_tel(itype)
            dname = f'fin_tel{itype}.jpg'
        case TYPE_FILE_NUMBER.SIX:
            img = ImageMaker(path, fname).make_last(config.PHONE_TEXT)
            dname = 'fin_last.jpg'
        case _:
            if extension in ('.mp4'):
                return fname
    if img:
        img.save(config.RESULT_DIR / dname, quality=100)
        print(f'{fname} > success > {config.RESULT_DIR / dname}')


if __name__ == "__main__":
    path = f'{config.W13_DIR}/'
    os.makedirs(config.RESULT_DIR, exist_ok=True)

    if len(sys.argv) == 1:
        fnames: list[str] = [
            fname.name for fname in Path(path).glob('*')
            if (not fname.name.startswith('.')) and ('.' in fname.name)
        ]
        fnames.sort(reverse=True)

        video_file_path_list = []
        for fname in fnames:
            video_file_name: str = file_maker(path, fname)
            if video_file_name:
                video_file_path_list.append(video_file_name)

        VideoMaker().make_video(video_file_path_list)
        with open(config.RESULT_DIR / 'city.txt', 'w', encoding='utf-8') as af:
            af.write(Location().get_cities())

    elif sys.argv[1] == '-v':
        video_file_path_list: list[str] = [
            fname.name for fname in Path(path).glob('*')
            if fname.name.split('.')[-1] == 'mp4'
        ]
        VideoMaker().make_video(video_file_path_list)

    elif sys.argv[1] == '-f':
        fname: str = sys.argv[2]
        itype: str = sys.argv[3]

        if len(sys.argv) >= 5:
            text: str = ' '.join(sys.argv[4:])

        if itype == TYPE_IMAGE.MAIN:
            img = ImageMaker(path, fname).make_main(config.TITLE)
            dname = 'fin_main.jpg'
        elif itype == TYPE_IMAGE.BEAF:
            img = ImageMaker(path, fname).make_beaf(text)
            dname = f'fin_{text}.jpg'
        elif itype in (TYPE_IMAGE.TEL1, TYPE_IMAGE.TEL2):
            img = ImageMaker(path, fname).make_tel(itype)
            dname = f'fin_{itype}.jpg'
        elif itype == TYPE_IMAGE.LAST:
            img = ImageMaker(path, fname).make_last(config.PHONE_TEXT)
            dname = 'fin_last.jpg'

        try:
            img.save(config.RESULT_DIR / dname, quality=100)
            print(f'{fname} > success > {config.RESULT_DIR / dname}')
        except Exception as e:
            print(f'++ [{itype}] ERROR: {e}')
