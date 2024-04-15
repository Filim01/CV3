import cv2

# 이미지 로드
image = cv2.imread('self.jpg')

if image is None:
    print("이미지를 읽을 수 없다.")
else:
    # 원하는 세로 길이 설정
    target_height = 700

    # 이미지의 현재 높이와 너비 가져오기
    height, width = image.shape[:2]

    # 비율에 따라 가로 길이 계산
    target_width = int((target_height / height) * width)

    # 이미지 크기 조정
    resized_image = cv2.resize(image, (target_width, target_height))

    # GaussianBlur 함수를 사용하여 가우시안 블러 적용 (sigma = 1, 3, 5)
    sigma_values = [1, 3, 5]
    for sigma in sigma_values:
        blurred_image = cv2.GaussianBlur(resized_image, (5, 5), sigmaX=sigma)

        # Sigma 값과 함께 텍스트 추가
        text = f'Sigma = {sigma}'
        cv2.putText(blurred_image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # 결과 이미지 출력
        cv2.imshow('Gaussian Blur', blurred_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
