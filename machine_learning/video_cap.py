import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue=np.array([50,50,50])
    dark_blue=np.array([180,255,150])

    mask=cv2.inRange(hsv,lower_blue,dark_blue)
    res=cv2.bitwise_and(frame, frame,mask=mask)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dialation=cv2.dilate(mask,kernel,iterations=1)
    
    
    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(res,-1,kernel)
    blur=cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow("frame",frame)
    cv2.imshow("erode",erosion)
    cv2.imshow("dialation",dialation)
    #cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    #cv2.imshow("smoothed",smoothed)
    #cv2.imshow("blur",blur)


    k=cv2.waitKey(5) & 0x80
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()