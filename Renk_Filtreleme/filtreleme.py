import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90,50,50])
yuksek = np.array([130,255,255])

kernel = np.ones((15,15),dtype=np.float32) / 225 #15 değerli arrayi 255e bölüyoruz.
def main():
    while True:
        ret,goruntu = kamera.read()
        hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, dusuk, yuksek) #maskelenmiş görsel
        son_resim = cv2.bitwise_and(goruntu,goruntu,mask=mask)

        # SMOOTHED (Yumuşatma)
        smoothed = cv2.filter2D(son_resim,-1,kernel)
        cv2.imshow("Yumusatilmis Gorsel",smoothed)

        #Blur
        blur = cv2.GaussianBlur(son_resim,(15,15),0)

        #Median
        median = cv2.medianBlur(son_resim,15)

        #Bilateral
        bilateral = cv2.bilateralFilter(son_resim,15,75,75)


        cv2.imshow("Mask", mask)
        cv2.imshow("Bilateral", bilateral)
        cv2.imshow("Median", median)
        cv2.imshow("Blur", blur)
        cv2.imshow("Ana (BGR) Kamera",goruntu)
        cv2.imshow("Hsv (HUE,STRATION,VALUE) Kamera", hsv)
        cv2.imshow("Son resim", son_resim)



        if cv2.waitKey(25) & 0xFF ==ord('q'):
            break

    kamera.relaese()
    cv2.destroyAllWindows()

print(kernel)
if __name__ == "__main__":
    main()

