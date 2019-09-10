import cv2
import numpy as np

resim = cv2.imread("main.jpg")
cv2.rectangle(resim, (45,150), (180,20), [0,0,255],3)
cv2.imshow("Main",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()