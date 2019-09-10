import cv2
import numpy as np

resim = cv2.imread("main.jpg")
cv2.imshow("Main",resim)

#Resmi Uzatma
uzatilan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
cv2.imshow("Main UZATMA",uzatilan_resim)

#Resmi Aynalama
aynalanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow("Main AYNALAMA",aynalanan_resim)

#Resmi Tekrar Etme
tekrarlanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
cv2.imshow("Main TEKRARLAMA",tekrarlanan_resim)

#Resmi Etrafını Sarma
etrafli_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT)
cv2.imshow("Main SARMA",etrafli_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()