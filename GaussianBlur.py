import cv2
import matplotlib.pyplot as plt

# 입력 이미지 파일 경로
img_file = "self.jpg"

# 이미지 컬러로 읽기 (원본 이미지)
img = cv2.imread(img_file)

if img is not None:
    # 가우시안 블러 적용
    Gausian_img1 = cv2.GaussianBlur(img, (0, 0), 1)
    Gausian_img2 = cv2.GaussianBlur(img, (0, 0), 3)
    Gausian_img3 = cv2.GaussianBlur(img, (0, 0), 5)

    # Matplotlib을 사용하여 이미지 표시
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # BGR에서 RGB로 변환하여 표시

    plt.subplot(2, 2, 2)
    plt.title("Sigma = 1")
    plt.imshow(cv2.cvtColor(Gausian_img1, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 3)
    plt.title("Sigma = 3")
    plt.imshow(cv2.cvtColor(Gausian_img2, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 4)
    plt.title("Sigma = 5")
    plt.imshow(cv2.cvtColor(Gausian_img3, cv2.COLOR_BGR2RGB))

    plt.tight_layout()  # 레이아웃 조정
    plt.show()

    # OpenCV를 사용하여 이미지 표시
    cv2.imshow("Gaussian Sigma = 1", Gausian_img1)
    cv2.imshow("Gaussian Sigma = 3", Gausian_img2)
    cv2.imshow("Gaussian Sigma = 5", Gausian_img3)
    cv2.waitKey(0)  # 키 입력 대기 (0은 무한대기)
    cv2.destroyAllWindows()

else:
    print("No image file.")

print('Program terminated.')








# import cv2
#
# # 이미지 로드
# image = cv2.imread('self.jpg')
#
# if image is None:
#     print("이미지를 읽을 수 없다.")
# else:
#     # 원하는 세로 길이 설정
#     target_height = 700
#
#     # 이미지의 현재 높이와 너비 가져오기
#     height, width = image.shape[:2]
#
#     # 비율에 따라 가로 길이 계산
#     target_width = int((target_height / height) * width)
#
#     # 이미지 크기 조정
#     resized_image = cv2.resize(image, (target_width, target_height))
#
#     # GaussianBlur 함수를 사용하여 가우시안 블러 적용 (sigma = 1, 3, 5)
#     sigma_values = [1, 3, 5]
#     for sigma in sigma_values:
#         blurred_image = cv2.GaussianBlur(resized_image, (5, 5), sigmaX=sigma)
#
#         # Sigma 값과 함께 텍스트 추가
#         text = f'Sigma = {sigma}'
#         cv2.putText(blurred_image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
#         # 결과 이미지 출력
#         cv2.imshow('Gaussian Blur', blurred_image)
#         cv2.waitKey(0)
#
#     cv2.destroyAllWindows()
