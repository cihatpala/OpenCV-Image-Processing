import cv2
import numpy as np

goruntu = cv2.VideoCapture(0)

dusuk = np.array([88,50,50])
yuksek = np.array([130,255,255])

def main():
    while True:
        ret,kamera = goruntu.read()
        hsv = cv2.cvtColor(kamera,cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv,dusuk,yuksek)
        son_resim = cv2.bitwise_and(kamera,kamera,mask=mask)

        kernel = np.ones((5,5),np.uint8)

        erosion = cv2.erode(mask,kernel,iterations=1)
        diolation = cv2.dilate(mask,kernel,iterations=1)

        opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
        closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

        cv2.imshow("Ana (BGR) Kamera",kamera)
        cv2.imshow("OPENING",opening)
        cv2.imshow("CLOSING",closing)
        cv2.imshow("Hsv (HUE,STRATION,VALUE) Kamera", hsv)
        cv2.imshow("Son Goruntu", son_resim)
        cv2.imshow("Erosion", erosion)
        cv2.imshow("Diolation", diolation)




        if cv2.waitKey(25) & 0xFF ==ord('q'):
            break

    kamera.relaese()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

