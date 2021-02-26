import cv2

img_path = "img/icon.jpg"

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
# cv2.namedWindow('attention', cv2.WINDOW_KEEPRATIO)
# cv2.setWindowProperty('attention', cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
cv2.imshow("attention", img)
# cv2.waitKey(2000)
cv2.waitKey(0)
cv2.destroyAllWindows()