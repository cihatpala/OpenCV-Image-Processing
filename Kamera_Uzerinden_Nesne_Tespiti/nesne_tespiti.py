import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,kare = kamera.read()
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    nesne = cv2.imread("faber_goruntu.png",0)

    w , h = nesne.shape
    res = cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED) #eşleştirme fonksiyonu
    esik_degeri = 0.7
    loc = np.where(res > esik_degeri)
    for i in  zip(*loc[::-1]):
        cv2.rectangle(kare,i,(i[0]+h,i[1]+w),(0,255,0),2)
        cv2.putText(kare,"Faber Castell 0.7 Uc",(i[0]+20,i[1]+100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)





    cv2.imshow("Kameradan Gelen Goruntu",kare)

    if cv2.waitKey(25) & 0xFF==ord('d'):
        break

kamera.release()
cv2.destroyAllWindows()