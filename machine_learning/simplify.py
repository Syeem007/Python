import cv2
import numpy as np

img=cv2.imread("bookpage.jpg")
retval,threshold=cv2.threshold(img,10,255,cv2.THRESH_BINARY)

cv2.imshow("original",img)
cv2.imshow("threshhold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
