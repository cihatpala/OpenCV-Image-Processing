import cv2
import numpy as np

def main():
    kamera = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID") #Format belirleme işlemi
    kayit = cv2.VideoWriter("kayit.mp4",fourcc,30,(680,480))

    while True:
        ret,goruntu = kamera.read()
        cv2.imshow("GORUNTU",goruntu)

        if ret == True:
            kayit.write(goruntu)

        if cv2.waitKey(25) & 0xFF ==ord('q'):
            break

    kamera.relaese()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

