import cv2
import numpy as np

# 입력 이미지 파일 경로
img_file = "self.jpg"
# 이미지 읽기
img = cv2.imread(img_file)

if img is not None:
    #kernel = np.zeros((5, 5), dtype=np.float64) / 25.
    kernel = np.ones((5, 5), dtype=np.float64) / 25
    kernel[0, :] = [-1, -2, -3, -2, -1]
    kernel[1, :] = [-2, -4, -6, -4, -2]
    kernel[2, :] = [0, 0, 0, 0, 0]
    kernel[3, :] = [2, 4, 6, 4, 2]
    kernel[4, :] = [1, 2, 3, 2, 1]

    print(kernel)

    filtered_img = cv2.filter2D(img, -1, kernel)

    cv2.imshow("filtered_img (cv2.filter2D)", filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No image file.")

print('program is terminated')






# import cv2
# import numpy as np
#
# # 이미지 로드
# image = cv2.imread('self.jpg')
#
# if image is None:
#     print("이미지를 읽을 수 없습니다. 파일 경로를 확인하세요.")
# else:
#     # 세로 길이가 너무 길어서 조정이 필요함
#     new_height = 700  # 원하는 세로 길이 설정 (예: 500 픽셀)
#
#     # 이미지의 현재 높이와 너비 가져오기
#     height, width = image.shape[:2]
#
#     # 비율에 맞게 가로 길이 계산
#     new_width = int(width * (new_height / height))
#
#     # 이미지 크기 조정
#     resized_image = cv2.resize(image, (new_width, new_height))
#
#     # 수평 에지 필터 (Sobel) 생성
#     kernel_edge_horizontal = np.array([
#         [-1, -2, -3, -2, -1],
#         [-2, -4, -6, -4, -2],
#         [0, 0, 0, 0, 0],
#         [2, 4, 6, 4, 2],
#         [1, 2, 3, 2, 1]
#     ], dtype=np.float32)
#
#     # 수평 에지 필터 (Sobel) 적용
#     filtered_edge_horizontal = cv2.filter2D(resized_image, -1, kernel_edge_horizontal)
#
#     # 결과 이미지 출력
#     cv2.imshow('Filtered2D Image', filtered_edge_horizontal)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
