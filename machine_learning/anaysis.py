import numpy as np
import cv2
import os

route=r'watch.jpg'
img=cv2.imread(os.path.abspath(route),cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
watch_face=img[37:111,107:194]
img[0:74,0:87]=watch_face
print(px)
img[100:150,100:150]=[255,255,255]
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()