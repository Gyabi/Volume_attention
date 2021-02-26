import cv2
import numpy as np

rgb_img_path = "img/icon_rgb.jpg"
min_main_color = np.array([1,200,200])
max_main_color = np.array([100,255,255])
rgb_img = cv2.imread(rgb_img_path)

a_data = np.ones((rgb_img.shape[0],rgb_img.shape[1]))
mask = np.ones((rgb_img.shape[0],rgb_img.shape[1]))

# 指定した色相の範囲内の要素を1に変更
for i,a in enumerate(rgb_img):
    for j,b in enumerate(a):
        if ((min_main_color <= b).all() and (max_main_color >= b).all()):
            mask[i,j] = 0



cv2.imshow("attention", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
