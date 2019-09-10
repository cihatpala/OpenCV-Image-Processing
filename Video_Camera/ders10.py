import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
kamera.set(3, 600)
kamera.set(4, 600)

def boyutlandirma(kare, yuzde=75):
    genislik = int(kare.shape[1]*yuzde/100)
    yukseklik = int(kare.shape[0]*yuzde/100)
    boyut =(genislik,yukseklik)
    return cv2.resize(kare,boyut,interpolation = cv2.INTER_AREA)

def main():
    while True:
        ret,kare = kamera.read()
        kare_boyutlu = boyutlandirma(kare)
        kamera_gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

        cv2.imshow("Gri Kamera Görüntüsü", kamera_gri)
        cv2.imshow("Kamera",kare)
        cv2.imshow("Boyutlandırılmış",kare_boyutlu)
        print(kare[100,200])
        #cv2.rectangle(kamera, (100, 200), (200, 100), (255, 0, 0), 2)
        bolge = kare[0:300,0:300]
        cv2.imshow("Bolge",bolge) #kameradan bir kesit gösterilir
        if cv2.waitKey(25) & 0xFF ==ord('q'):
            break

    kamera.relaese()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

