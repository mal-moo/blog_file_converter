from enum import Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class TYPE_FILE_NUMBER(StrEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"


class TYPE_IMAGE(StrEnum):
    MAIN = "main"
    BEAF = "beaf"
    TEL1 = "tel1"
    TEL2 = "tel2"
    LAST = "last"