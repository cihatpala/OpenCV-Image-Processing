import cv2
import numpy as np


#ret,kare =kamera.read()

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
goz_casc = cv2.CascadeClassifier("haarcascade_eye.xml")
resim = cv2.imread("yuz_erkek1.jpg")
gri_ton = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
gozler = goz_casc.detectMultiScale(gri_ton,1.09,4)

yuzler = yuz_casc.detectMultiScale(gri_ton,1.09,4)

#print(yuzler)

for (x,y,w,h) in yuzler:
    cv2.rectangle(resim,(x,y),(x+w,y+h),(0,0,255),3)
    yuz_bolgesi = resim[y:y + h, x:x + w]
    gri_yuz_bolgesi = cv2.cvtColor(yuz_bolgesi, cv2.COLOR_BGR2GRAY)
    gozler = goz_casc.detectMultiScale(gri_yuz_bolgesi, 1.1, 4)
    for (a, b, c, d) in gozler:
        cv2.rectangle(yuz_bolgesi, (a, b), (a + c, b + d), (0, 255, 0), 2)

resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("Resim", resim)

cv2.waitKey(0)
#kamera.release()
cv2.destroyAllWindows()