from camera.camera_class import camera
import time

# 고속카메라 이미지 저장하는 객체 생성 : image_saver
image_saver = camera.ImageSaver()

# 고속카메라 연결 함수 실행
image_saver.cam_open()

# 이미지 400개 저장(초당 196장, 실제 사용하는 프로그램에서 초당 100장 저장하도록 수정)
for i in range(400):
    # 이미지를 jpeg 파일로 저장하는 함수 실행
    # 파일 이름이 중복되어 이미지가 1개만 저장되는 문제 해결하기 위해 파일 번호 추가
    # save_images(파일 개수, 파일 번호)
    # ex) image_saver.save_images(1, 2) -> 20230524_15시45분03초_img_2 와 같이 파일 1개 생성
    # ex) image_saver.save_images(2, 2) -> 20230524_15시45분03초_img_2_1, 20230524_15시45분03초_img_2_2 와 같이 파일 2개 생성
    image_saver.save_images(1, i)

# 아래는 예시
# 무한 반복문에서는 아래와 같이 사용하면 초당 100장 저장(약간의 오차 발생)
###################################################################
# last_time = time.perf_counter()
# num_img_to_save = 1
# img_num = 1

# while True:
#     image_saver.save_images(num_img_to_save, img_num)

#     if img_num == 100:
#         img_num = 1
#         # break
#     else:
#         img_num += 1

#     # sleep until 1 second has elapsed since the last loop
#     elapsed_time = time.perf_counter() - last_time
#     if elapsed_time < 0.01:
#         time.sleep(0.01 - elapsed_time)
#     else:
#         time.sleep(0.01)
#     last_time = time.perf_counter()
###################################################################

# 고속카메라 연결 종료 함수 실행
image_saver.cam_close()