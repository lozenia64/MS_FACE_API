import requests
from io import BytesIO
from time import sleep
import cognitive_face as CF
from picamera import PiCamera
from PIL import Image, ImageDraw

camera = PiCamera()
camera.rotation = 180 # 180도 회전. 본인 카메라 환경에 맞게 사용

KEY = 'KEY' # 자신의 Cognitive Services API KEY
CF.Key.set(KEY)

BASE_URL = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/' # 자신의 지역 설정
CF.BaseUrl.set(BASE_URL)

IMG_URL = '/home/pi/MSFACE/image.jpg' # 이미지 파일의 경로

while True:
    camera.start_preview() # 카메라 사용 시작
    camera.capture('/home/pi/MSFACE/image.jpg') # 현재 카메라 화면을 이미지 파일로 저장
    camera.stop_preview() # 카메라 사용 종료

    faces = CF.face.detect(IMG_URL,True,False,'age,gender') # 저장된 이미지에서 얼굴 검출
    for face in faces:
        print(face['faceAttributes']) # 감지된 얼굴의 속성 값 출력