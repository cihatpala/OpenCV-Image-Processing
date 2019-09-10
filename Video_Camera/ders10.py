import cv2
import numpy as np


kamera = cv2.VideoCapture(0)
while True:
    ret,kare = kamera.read()

    cv2.imshow("Video",kare)
    print(kare[100,200])
    #cv2.rectangle(kamera, (100, 200), (200, 100), (255, 0, 0), 2)
    if cv2.waitKey(25) & 0xFF ==ord('q'):
        break

kamera.relaese()
cv2.destroyAllWindows()

