import cv2
import numpy as np
# aik hi window ma show kran ka liya
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# to corner each symbol in img to detect each symbol
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgcon,cnt,-1,(255,0,0),1)
            # border to mark krna drawcontours sa

            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print("hello",len(approx))
            obj = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgcon,(x,y),(x+w,y+h),(0,255,0),1)
            if obj == 3 : objecttype = "tri"
            elif obj<15 : objecttype ="circle"
            else: objecttype = "None"
            cv2.putText(imgcon,objecttype,(x + (w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,128,0),1)
            # ya x or y wali bat center dhoonf ri thi us ka
            # us aik symbol ko box ma display krna


img = cv2.imread("Resources/coloured-infinite-symbols-collection_1025-925.jpg")
imgcon = img.copy()
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray,(7,7),1)


imgcanny = cv2.Canny(imgblur,100,100)
imgblank= np.zeros_like(img)
#uper wala black blank img ka liya haa...
# display in stack and 1 is size of window can be decimal
getContours(imgcanny)
Stackimg = stackImages(1,([img,imgblur,imggray,],
                         [imgcanny,imgcon,imgblank]))
#cv2.imshow("Original",img)
#cv2.imshow("Gray",imggray)
#cv2.imshow("Blur",imgblur)
cv2.imshow("Full",Stackimg)
cv2.waitKey(0)
