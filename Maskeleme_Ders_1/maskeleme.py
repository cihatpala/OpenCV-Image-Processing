import cv2
import numpy as np



def main():
    kesilecek = cv2.imread("siyahli.jpg")
    arkaplan = cv2.imread("arkaplan.jpg")

    kesilecek_gri = cv2.cvtColor(kesilecek, cv2.COLOR_BGR2GRAY) #Burada renkli fotoğrafı 0-255 değer aralığındaki gri fotoğrafa dönüştürdük.

    genislik, yukseklik, kanal = kesilecek.shape
    yapistirilacak_yer = arkaplan[0:genislik,0:yukseklik]
    #cv2.imshow("Yapıştırılacak Bölge", yapistirilacak_yer)

    ret, mask = cv2.threshold(kesilecek_gri, 10, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Masklanmış Resim", mask)

    mask_inver = cv2.bitwise_not(mask) #masklanmış resmin ters masklanmışını almak.
    cv2.imshow("Ters Masklanmış Resim", mask_inver)

    background_add = cv2.bitwise_and(yapistirilacak_yer,yapistirilacak_yer,mask=mask_inver)
    cv2.imshow("Ters Masklanmis ile Birlestirme", background_add)

    toplam = cv2.add(background_add, kesilecek)
    cv2.imshow("Ters Mask'ın eklenmiş hali + Eklenen orjinal Foto", toplam)

    arkaplan[0:yukseklik,0:genislik] = toplam
    cv2.imshow("En son Eklenmis Hali", arkaplan)




    #print(genislik, yukseklik, kanal) #değerleri görmek için.
    #print(kesilecek_gri[210,100]) #kesilen gri fotoğrafın 210'a 100. pikselindeki gri değeri okumak (görmek) için

    #cv2.imshow("Kesilecek Resim", kesilecek)
    #cv2.imshow("Arkaplan Resmi", arkaplan)
    #cv2.imshow("Kesilecek Gri", kesilecek_gri)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

