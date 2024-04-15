import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('self.jpg')

if image is None:
    print("이미지를 읽을 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 세로 길이가 너무 길어서 조정이 필요함
    new_height = 700  # 원하는 세로 길이 설정 (예: 500 픽셀)

    # 이미지의 현재 높이와 너비 가져오기
    height, width = image.shape[:2]

    # 비율에 맞게 가로 길이 계산
    new_width = int(width * (new_height / height))

    # 이미지 크기 조정
    resized_image = cv2.resize(image, (new_width, new_height))

    # 수평 에지 필터 (Sobel) 생성
    kernel_edge_horizontal = np.array([
        [-1, -2, -3, -2, -1],
        [-2, -4, -6, -4, -2],
        [0, 0, 0, 0, 0],
        [2, 4, 6, 4, 2],
        [1, 2, 3, 2, 1]
    ], dtype=np.float32)

    # 수평 에지 필터 (Sobel) 적용
    filtered_edge_horizontal = cv2.filter2D(resized_image, -1, kernel_edge_horizontal)

    # 결과 이미지 출력
    cv2.imshow('Filtered2D Image', filtered_edge_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
