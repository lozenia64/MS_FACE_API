import requests
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF

KEY = 'KEY' # 자신의 Cognitive Services API KEY
CF.Key.set(KEY)

BASE_URL = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/' # 자신의 지역에 해당하는 URL
CF.BaseUrl.set(BASE_URL)

img_url = '/home/pi/MSFACE/im1.jpg' # 이미지 파일의 경로
faces = CF.face.detect(img_url,True,False,'age,gender') # 중요!
# detect 함수는 4가지의 매개변수를 갖는다.
# 첫 번째 인자 : 이미지파일
# 두 번째 인자 : face_id의 반환 여부
# 세 번째 인자 : landmarks(눈,코,입 등의 위치)의 반환 여부
# 네 번째 인자 : 반환할 속성(연령,성별 등)

print(faces[0]['faceAttributes']) # 터미널 창에 속성값들을 출력

# 인식된 얼굴에 네모 박스 그리는 함수 작성
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

img = Image.open(img_url) # img 변수에 이미지 파일을 넣어준다.
draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red') # 인식된 얼굴들에 네모 박스 쳐주기

img.show() # 이미지 뷰어로 이미지 띄우기
