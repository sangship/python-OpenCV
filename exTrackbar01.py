import cv2
import numpy as np

# 트랙바에 사용될 콜백 함수 (필수, 하지만 여기서는 아무 작업도 하지 않음)
def on_Trackbar_R(x):
    print(f'x: {x}')
    
def on_Trackbar_G(x):
    print(f'g: {x}')

def on_Trackbar_B(x):
    print(f'b: {x}')



# 빈 이미지 생성
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 트랙바 생성 (초기값 설정: R = 100, G = 150, B = 200)
cv2.createTrackbar('R', 'image', 100, 255, on_Trackbar_R)
cv2.createTrackbar('G', 'image', 150, 255, on_Trackbar_G)
cv2.createTrackbar('B', 'image', 200, 255, on_Trackbar_B)

while True:
    # 트랙바에서 현재 값 가져오기
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    # 이미지에 색상 값 적용
    img[:] = [b, g, r]

    # 이미지 표시
    cv2.imshow('image', img)

    # 'ESC' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
