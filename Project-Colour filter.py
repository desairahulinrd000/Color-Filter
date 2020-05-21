import cv2
import numpy as np
low = np.array([100, 50, 50])
high = np.array([140, 255, 255]) 
def emptyfunction(pos1):
    pass
windowname1="Trackbar"
windowname2="Image"
cv2.namedWindow(windowname1,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(windowname2,cv2.WINDOW_AUTOSIZE)
img=cv2.imread("C:\\Users\\lenovo\\Desktop\\b.png")
img = cv2.resize(img,(560,360))
cv2.createTrackbar('Low Blue',windowname1,0,255,emptyfunction)
cv2.createTrackbar('Low Green',windowname1,0,255,emptyfunction)
cv2.createTrackbar('Low Red',windowname1,0,255,emptyfunction)
cv2.createTrackbar('High Blue',windowname1,0,255,emptyfunction)
cv2.createTrackbar('High Green',windowname1,0,255,emptyfunction)
cv2.createTrackbar('High Red',windowname1,0,255,emptyfunction)
ret=True
while ret:
    lblue=cv2.getTrackbarPos('Low Blue', windowname1)
    lgreen=cv2.getTrackbarPos('Low Green', windowname1)
    lred=cv2.getTrackbarPos('Low Red', windowname1)
    hblue=cv2.getTrackbarPos('High Blue', windowname1)
    hgreen=cv2.getTrackbarPos('High Green', windowname1)
    hred=cv2.getTrackbarPos('High Red', windowname1)
    low = np.array([lblue, lgreen,lred])
    high = np.array([hblue, hgreen, hred])   
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    image_mask = cv2.inRange(hsv, low, high)
    output = cv2.bitwise_and(img, img, mask = image_mask)
    cv2.imshow("original",img)
    cv2.imshow("Mask",image_mask)
    cv2.imshow(windowname2,output)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
