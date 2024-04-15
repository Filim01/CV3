import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('self.jpg')

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    # 이미지 크기 조정
    target_height = 700
    height, width = image.shape[:2]
    target_width = int((target_height / height) * width)
    resized_image = cv2.resize(image, (target_width, target_height))

    # 5x5 평균 필터 커널 생성 (모든 요소가 1/25)
    kernel_average = np.ones((5, 5), dtype=np.float32) / 25.0

    # opencv의 boxFilter() 함수를 사용하여 평균 필터 적용
    filtered_average = cv2.boxFilter(resized_image, -1, (5, 5))

    # 결과 이미지 출력
    cv2.imshow('Filtered Image (Average)', filtered_average)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
