import cv2
import numpy as np

def main():
    resim = np.zeros((600,600,3),dtype="uint8")
    resim.fill(255) #oluşturduğumuz siyah arkaplanı beyaz yapar

    cv2.line(resim,(100,100),(500,500),(255,0,150),3) #resim değişkeninin içerisindeki resme bir çizgi çeker.
    cv2.line(resim,(100,500),(500,100),(255,0,150),3)  # resim değişkeninin içerisindeki resme bir çizgi çeker.
    cv2.line(resim, (100, 300), (500, 300), (255, 0, 150), 3)  # resim değişkeninin içerisindeki resme bir çizgi çeker.
    cv2.circle(resim,(300,300),(200),(0,255,0),3)
    cv2.putText(resim,"Naber?",(220,100),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
    cv2.rectangle(resim,(100,500),(500,100),(0,0,0),2)

    cv2.imshow("Calisma Alani", resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()