## mr_rvc_datapreprocessing
AI 커버 컨텐츠에 대해 RVC 음성합성기술 모델을 사용하는데 있어서
완성도와 퀄리티를 높일 수 있도록 도와주는 API입니다.

# 데이터셋 정제
학습하고자하는 목소리를 HZ와 Second로 나눠 학습에 필요로하는 모델 조건에 대응하기 위한 기능입니다.

# MR 분리, 합성
분리 : 노래 또는 영상의 음성과 배경음(노이즈)을 나눠 모델학습의 퀄리티에 기여하는 기능입니다.
합성 : 음성과 배경음을 합성하여 하나의 결과물로 만드는 목적을 가진 기능입니다.

예시 사용법
1. 데이터셋을 정제하여 RVC로 모델 생성
2. 생성 된 동안 미리 AI 커버 할 노래 MR분리
3. MR분리에서 나온 보이스를 만들어진 모델로 합성
4. 합성된 음성을 기존 노래 배경음과 합성하여 결과물 완성

## 개발 환경

운영 체제 : 윈도우</br>
언어 : Python v3.9</br>
프레임워크 : FastAPI</br>

## GetStart

1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. FastAPI 실행
```zsh
uvicorn main:app
```
