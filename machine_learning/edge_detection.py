import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    laplacin=cv2.Laplacian(frame, cv2.CV_8U)
    edges=cv2.Canny(frame,0,00)
    #cv2.imshow("original",frame)
    #cv2.imshow("laplacian",laplacin)
    cv2.imshow("edge",edges)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cv2.release()