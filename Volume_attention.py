import cv2
from playsound import playsound
from screeninfo import get_monitors
import threading

param = {
    "img_path":"img/icon.jpg",
    "use_moniter":1,
    "voice_path":"voice/alert.mp3"
}

# 画像を表示する関数
def image_show(param):
    img = cv2.imread(param["img_path"])
    for m in get_monitors():
        if m.name == "\\\\.\\DISPLAY" + str(param["use_moniter"]):
            moniter_height = m.height
            moniter_width = m.width
    img = cv2.resize(img, (int(img.shape[0]*1.5),int(img.shape[1]*1.5)))
    cv2.imshow("attention", img)
    cv2.moveWindow("attention", int(moniter_width/2-img.shape[0]/2), int(moniter_height/2-img.shape[1]/2))
    cv2.waitKey(2500)
    cv2.destroyAllWindows()

# 音声を出力する関数
def voice_out(param):
    playsound(param["voice_path"])

thread1 = threading.Thread(target=image_show, args=(param, ))
thread2 = threading.Thread(target=voice_out, args=(param, ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

