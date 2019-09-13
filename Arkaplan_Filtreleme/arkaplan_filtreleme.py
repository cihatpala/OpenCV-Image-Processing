import cv2
import numpy as np

def main():
    resim = cv2.imread("filtrelenecek.jpg")

    mask = np.zeros(resim.shape[:2], np.uint8)

    bgdModel = np.zeros((1,65), dtype=np.float64)
    fgdModel = np.zeros((1,65), dtype=np.float64)

    rect = (100,0,500,900)

    cv2.grabCut(resim, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==0) | (mask==2),0,1).astype(np.uint8)

    resim = resim*mask2[:,:,np.newaxis]
    cv2.imshow("Resim Masklı ",resim)




    cv2.imshow("Filtrelenmemis Resim",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()