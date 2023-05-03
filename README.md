# blog_file_converter
```
.
├── contents.env  # 작업 내용 수정 파일
├── result  # 결과물 폴더
│   └── 2023-05-03
│       ├── city.txt
│       ├── fin.mp4
│       ├── fin_last.jpg
│       ├── fin_main.jpg
│       ├── fin_tel1.jpg
│       ├── fin_tel2.jpg
│       ├── fin_시공전.jpg
│       └── fin_시공후.jpg
├── run.sh  # 실행 파일
├── src  # 소스코드
│   ├── config
│   │   └── config.py
│   ├── const
│   │   └── enum.py
│   ├── main.py
│   ├── service
│   │   ├── image_maker.py
│   │   └── video_maker.py
│   └── utils
│       ├── drawer.py
│       └── location.py
├── ttf  # 폰트 폴더
│   ├── The Jamsil 1 Thin.ttf
│   ├── The Jamsil 2 Light.ttf
│   ├── The Jamsil 3 Regular.ttf
│   ├── The Jamsil 4 Medium.ttf
│   ├── The Jamsil 5 Bold.ttf
│   └── The Jamsil 6 ExtraBold.ttf
└── w13  # 원본 사진 및 영상 폴더
    ├── 1.jpeg
    ├── 2.jpeg
    ├── 3.jpeg
    ├── 4.jpeg
    ├── 5.jpeg
    ├── 6.jpeg
    ├── KakaoTalk_Video_2023-04-29-00-23-26.mp4
    └── KakaoTalk_Video_2023-04-29-00-23-30.mp4
```

1. w13 폴더에 사진 1~6.jpeg 와 영상 2개를 넣어놓는다.
2. ttf 폴더에 폰트 파일을 넣어놓는다.
3. contents.env에 작업 내용을 수정하여 저장한다.
4. ./run.sh 또는 bash run.sh로 실행한다.


    (단, run.sh에 실행권한이 부여되어있어야함)
5. 결과파일은 result 폴더에서 확인한다.

    (결과파일은 자동으로 생성된다.)
