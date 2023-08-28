# blog_file_converter
```
.
├── build.sh  # 환경 셋팅 스크립트
├── contents.env  # 작업 내용 수정 파일
├── run.sh  # 실행 스크립트
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
└── w13  # 원본 사진 및 영상 업로드하는 곳 / 결과 파일 저장되는 곳
    ├── 1.jpeg
    ├── 2.jpeg
    ├── 3.jpeg
    ├── 4.jpeg
    ├── 5.jpeg
    ├── KakaoTalk_Video_2023-04-29-00-23-26.mp4
    └── KakaoTalk_Video_2023-04-29-00-23-30.mp4
```

1. ./build.sh 또는 bash build.sh를 실행하여 가동환경 셋팅을 설정한다.
2. w13 폴더에 사진 1~5.jpeg 와 영상 2개를 넣어놓는다.
3. contents.env에 작업 내용을 수정하여 저장한다.
4. ./run.sh 또는 bash run.sh로 실행한다.
5. 결과파일은 w13 폴더에서 확인한다.
    ```
        ├── city.txt
        ├── fin.mp4
        ├── fin_main.jpg
        ├── fin_tel1.jpg
        ├── fin_tel2.jpg
        ├── fin_After.jpg
        └── fin_Before.jpg
    ```