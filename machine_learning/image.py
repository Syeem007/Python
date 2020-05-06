##for image file create step 1

import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
route=r'watch.jpg'
img=cv2.imread(os.path.abspath(route),cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("watchgray.png",img)
#plt.imshow(img,cmap="gray",interpolation="bicubic")
#plt.plot([50,100],[80,100],"c",linewidth=5)
#plt.show()

