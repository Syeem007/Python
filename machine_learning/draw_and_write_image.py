#step2 for draw and write image
import os
import numpy as np
import cv2

route=r'watch.jpg'
img=cv2.imread(os.path.abspath(route),cv2.IMREAD_COLOR)  #import picture
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()