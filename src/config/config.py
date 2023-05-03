from datetime import datetime
from pydantic import BaseSettings
from pathlib import Path, PurePath


class MyConfig(BaseSettings):
    TITLE: list[str]
    PHONE_TEXT: list[str]
    NAME: str
    PHONE: str
    LOCATION: str = None

    DIR: Path = Path.cwd()
    SRC_DIR: Path = DIR / 'src'
    W13_DIR: Path = DIR / 'w13'
    RESULT_DIR: Path = DIR / 'result' / datetime.now().strftime('%Y-%m-%d')
    FONT_DIR: Path = DIR / 'ttf'
    IMG_SIZE: int = 1080

    FONT_FILE: str
    IMAGE_BORDER_COLOR_RGB: str
    TEXT_BORDER_COLOR_RGB: str
    TEXT_FILL_COLOR_RGB: str
    NAME_FILL_COLOR_RGB: str

    @property
    def IMAGE_BORDER_COLOR(self) -> tuple[int]:
        return tuple(map(int, self.IMAGE_BORDER_COLOR_RGB.split(',')))

    @property
    def TEXT_BORDER_COLOR(self):
        return tuple(map(int, self.TEXT_BORDER_COLOR_RGB.split(',')))

    @property
    def TEXT_FILL_COLOR(self):
        return tuple(map(int, self.TEXT_FILL_COLOR_RGB.split(',')))

    @property
    def NAME_FILL_COLOR(self):
        return tuple(map(int, self.NAME_FILL_COLOR_RGB.split(',')))

    @property
    def FONT(self) -> Path:
        return self.FONT_DIR / self.FONT_FILE

    class Config:
        env_pwd = PurePath(Path(__file__).absolute()).parent.parent.parent
        env_file = env_pwd / 'contents.env'
        env_file_encoding = 'utf-8'


config = MyConfig()
