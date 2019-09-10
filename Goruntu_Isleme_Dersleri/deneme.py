import cv2
import numpy as np

resim = cv2.imread("main.jpg")

b,g,r = cv2.split(resim)
cv2.imshow("Görüntü işleme ilk adımı",resim)
cv2.imshow("Blue Channel",b)
cv2.imshow("Green Channel",g)
cv2.imshow("Red Channel",r)

for i in range(100):
    print(b[i,i],(1,0,0))


cv2.waitKey(0)
cv2.destroyAllWindows()