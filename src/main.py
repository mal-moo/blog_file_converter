# brew install imagemagick or brew update && brew install imagemagick
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
import os
import sys
from pathlib import Path

from config.config import config
from const.enum import TYPE_FILE_NUMBER, TYPE_IMAGE
from service.image_maker import ImageMaker
from service.video_maker import VideoMaker
from utils.drawer import Drawer
from utils.location import Location


def make_image_by_type(filename: str, imagemaker: ImageMaker) -> str | None:
    img = None

    match filename:
        case TYPE_FILE_NUMBER.ONE:
            img = imagemaker.make_main(config.TITLE)
            dname = 'fin_main.jpg'
        case TYPE_FILE_NUMBER.TWO | TYPE_FILE_NUMBER.THREE:
            text = '작업 전' if filename == TYPE_FILE_NUMBER.TWO else '작업 후'
            img = imagemaker.make_beaf(text)
            dname = f'fin_{text}.jpg'
        case TYPE_FILE_NUMBER.FOUR | TYPE_FILE_NUMBER.FIVE:
            itype = '1' if filename == TYPE_FILE_NUMBER.FOUR else '2'
            img = imagemaker.make_tel(itype)
            dname = f'fin_tel{itype}.jpg'
        case TYPE_FILE_NUMBER.SIX:
            img = imagemaker.make_last(config.PHONE_TEXT)
            dname = 'fin_last.jpg'
        case _:
            pass

    if img is not None:
        img.save(config.W13_DIR / dname, quality=100)
        print(f'{filename} > success > {config.W13_DIR / dname}')


def total(path: str):
    filenames: list[str] = [
        fname.name for fname in Path(path).glob('*')
        if (not fname.name.startswith('.')) and ('.' in fname.name)
    ]
    filenames.sort(reverse=True)

    video_file_path_list = []
    IMAGE_EXTENSIONS = ['.jpg', '.jpeg']  # FIXME
    VIDEO_EXTENSIONS = ['.mp4']  # FIXME

    drawer = Drawer()
    imagemaker = ImageMaker(drawer=drawer)
    for filename in filenames:
        f, extension = os.path.splitext(filename)
        if extension in IMAGE_EXTENSIONS:
            imagemaker.setter(path=path, filename=filename)
            imagemaker.open_img()
            make_image_by_type(f, imagemaker)
        elif extension in VIDEO_EXTENSIONS:
            video_file_path_list.append(filename)
    # VideoMaker(drawer=drawer).make_video(video_file_path_list)

    with open(config.W13_DIR / 'city.txt', 'w', encoding='utf-8') as af:
        af.write(Location().get_cities())


def only_video(path: str):
    video_file_path_list: list[str] = [
        fname.name for fname in Path(path).glob('*')
        if fname.name.split('.')[-1] == 'mp4'
    ]
    VideoMaker().make_video(video_file_path_list)


def only_image(path: str):
    filename: str = sys.argv[2]
    itype: str = sys.argv[3]

    if len(sys.argv) >= 5:
        text: str = ' '.join(sys.argv[4:])

    if itype == TYPE_IMAGE.MAIN:
        img = ImageMaker(
            path=path,
            filename=filename,
            drawer=Drawer()
        ).make_main(config.TITLE)
        dname = 'fin_main.jpg'
    elif itype == TYPE_IMAGE.BEAF:
        img = ImageMaker(
            path=path,
            filename=filename,
            drawer=Drawer()
        ).make_beaf(text)
        dname = f'fin_{text}.jpg'
    elif itype in (TYPE_IMAGE.TEL1, TYPE_IMAGE.TEL2):
        img = ImageMaker(
            path=path,
            filename=filename,
            drawer=Drawer()
        ).make_tel(itype)
        dname = f'fin_{itype}.jpg'
    elif itype == TYPE_IMAGE.LAST:
        img = ImageMaker(
            path=path,
            filename=filename,
            drawer=Drawer()
        ).make_last(config.PHONE_TEXT)
        dname = 'fin_last.jpg'

    try:
        img.save(config.W13_DIR / dname, quality=100)
        print(f'{filename} > success > {config.W13_DIR / dname}')
    except Exception as e:
        print(f'++ [{itype}] ERROR: {e}')


def run():
    path = f'{config.W13_DIR}/'

    if len(sys.argv) == 1:
        total(path)
    elif sys.argv[1] == '-v':
        only_video(path)
    elif sys.argv[1] == '-f':
        only_image(path)


if __name__ == "__main__":
    run()
