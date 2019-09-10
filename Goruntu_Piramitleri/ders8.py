import cv2
import numpy as np
def main():
    resim = cv2.imread("main.jpg")
    zeros = np.zeros((400,400,3), dtype="uint8")

    cv2.rectangle(zeros,(100,300), (300,100),(0,0,255),3)
    cv2.imshow("Zeros", zeros)

    print(resim.shape) #normal fotoğrafın yükseklik, genişlik ve derinlik sayısı

    cv2.imshow("Main Fotoğraf",resim)


    iki_kat_buyuk = cv2.pyrUp(resim)
    cv2.imshow("İki Kat Büyük Main", iki_kat_buyuk)

    iki_kat_kucuk = cv2.pyrDown(resim)
    cv2.imshow("İki Kat Küçük Main", iki_kat_kucuk)

    print(iki_kat_kucuk.shape) #boyutları iki katına küçültülmüş yükseklik, genişlik ve derinlik sayısı

    print(iki_kat_buyuk.shape) #boyutları iki katına çıkmış yükseklik, genişlik ve derinlik sayısı

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
