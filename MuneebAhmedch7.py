import cv2
import numpy as np
# color detection in image
def empty(a):
    pass


path = 'Resources/image.png'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",480,350)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",161,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",32,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",154,255,empty)
cv2.createTrackbar("Val Min","TrackBars",91,255,empty)
cv2.createTrackbar("Val Max","TrackBars",221,255,empty)
while True:
    img = cv2.imread(path)
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_max,s_min,v_max,v_min)
    lower = np.array([h_min,s_min,v_min])
    higher = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,higher)
    result = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Picture ",img)
    cv2.imshow("Picture of mask ",mask)
    #sway to check colors
    cv2.imshow("Result",result)
    cv2.imshow("Color Detect",imghsv)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




