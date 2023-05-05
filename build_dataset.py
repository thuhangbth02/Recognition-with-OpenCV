# USAGE
# python build_dataset.py --output dataset/huy
""" Xây dựng dataset bằng cách chụp webcam """
import argparse
import cv2 
import os

# tim hieu ve dataset, cac buoc xu ly
# So luong du lieu: bao nhieu thu muc - 1 label (1 nhan). Kich thuoc cua tung anh, tinh ti le giua moi thu muc
# Xem cac anh co cung kich thuoc hay ko?
# vdu: cua Hang la 100, cua Huong la 200, ti le la 1/2 giua Hang va Huong tuong ung
# mo File Explorer, vao thu muc dataset, vao thu muc chua anh, click chuot phai chon properties


ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to output directory")
args = vars(ap.parse_args())

video = cv2.VideoCapture(0)
total = 0
while True:
    ret, frame = video.read()

    cv2.imshow("video", frame)  
    key = cv2.waitKey(1) & 0xFF
    # Thao tác lưu ảnh vào dataset 
    if key == ord("k"):
        p = os.path.sep.join([args["output"], "{}.png".format(str(total).zfill(5))])    # điền thêm số 0 bên trái cho đủ 5 kí tự
        cv2.imwrite(p, frame)
        total += 1
	# nhấn q để thoát
    elif key == ord("q"):
	    break

print("[INFO] {} face images stored".format(total))
video.release()
cv2.destroyAllWindows()