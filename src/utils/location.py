import random

from config.config import config


class Location:
    def __init__(self):
        self.city = config.LOCATION
        self.CITIES = {
            "경기": [
                "갈매", "고양", "과천", "광교", "광명", "광주", "구리", "군포", "남양주", "동두천", "동탄",
                "민락", "부천", "분당", "산본", "성남", "수원", "시흥", "안산", "안양", "양주", "여주",
                "옥정", "용인", "의왕", "의정부", "이천", "일산", "파주", "판교", "평택", "포천", "하남", "화성"
            ],
            "서울": [
                "강남", "고덕", "관악", "도봉", "동대문", "반포", "방배", "삼성", "서대문", "서초",
                "성북", "송파", "신사", "왕십리", "잠실", "종로", "천호", "청담"
            ],
            "인천": [
                "부평", "송도", "영종도", "청라"
            ],
            "천안": [
                "천안"
            ]
        }

    def get_cities(self):
        if not self.city:
            all_cities = self.CITIES['경기'] + self.CITIES['서울'] + self.CITIES['인천'] + self.CITIES['천안']
            ret = random.sample(all_cities, 30)
            ret_2 = random.sample(all_cities, 7)
        # elif self.city in ('경기', '경기도'):
        #     ret = random.sample(self.CITIES['경기'], 30)
        # elif self.city in ('서울', '서울특별시', '서울시'):
        #     ret = self.CITIES['서울'] + random.sample(self.CITIES['경기'], 12)
        # elif self.city in ('인천', '인천광역시'):
        #     ret = self.CITIES['인천'] + random.sample(self.CITIES['경기'], 26)
        # elif self.city == '천안':
        #     ret = self.CITIES['서울'] + random.sample(self.CITIES['경기'], 29)

        if ret:
            return ', '.join(ret) + ' 지역 등\n\n' + ', '.join(ret_2)
        else:
            return f'no match!!!! {self.city}'
