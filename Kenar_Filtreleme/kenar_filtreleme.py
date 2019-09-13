import cv2
import numpy as np

resim = cv2.imread("bilim_adamlari.jpg")

#Laplacian Filtreleme
laplacian = cv2.Laplacian(resim,cv2.CV_64F)
cv2.imshow("Laplacianlı Resim",laplacian)


cv2.imshow("Orjinal Resim",resim)

#Sobel Dikey
sobel_dikey = cv2.Sobel(resim,cv2.CV_64F,1,0,ksize=1)
cv2.imshow("Sobel Dikey",sobel_dikey)

#Sobel Yatay
sobel_yatay = cv2.Sobel(resim,cv2.CV_64F,0,1,ksize=1)
cv2.imshow("Sobel Yatay",sobel_yatay)

#Canny Filtreleme
canny = cv2.Canny(resim,500,200)
cv2.imshow("Canny Filtreleme",canny)

#Köşe Filtreleme
tahta = cv2.imread("satranc_tahtasi.jpg")
tahta_gri = cv2.cvtColor(tahta,cv2.COLOR_BGR2GRAY)
tahta_gri = np.float32(tahta_gri)
koseler = cv2.goodFeaturesToTrack(tahta_gri,500,0.1,10)
koseler = np.int0(koseler)
for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(tahta,(x,y),3,(255,0,0),-1)

cv2.imshow("Koseler",tahta)

cv2.waitKey(0)
cv2.destroyAllWindows()