import cv2
import numpy as np



def main():
    wp1 = cv2.imread("wallpaper1.jpg")
    wp2 = cv2.imread("wallpaper2.jpg")

    #print("On yuz değerleri --> Yuseklik : {} , Genislik : {} , Kanal Sayısı : {}".format(wp1.shape[0], wp1.shape[1], wp1.shape[2]))
    #print("On yuz değerleri --> Yuseklik : {} , Genislik : {} , Kanal Sayısı : {}".format(wp2.shape[0], wp2.shape[1], wp2.shape[2]))

    cv2.imshow("Wall Paper 1", wp1)
    cv2.imshow("Wall Paper 2", wp2)


    toplam = cv2.add(wp1,wp2)
    cv2.imshow("Toplam", toplam)

    agirlikli_toplam = cv2.addWeighted(wp1,0.9,wp2,0.1,0)
    cv2.imshow("Ağırlıklı Toplam", agirlikli_toplam)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

