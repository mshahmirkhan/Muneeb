import cv2
import numpy as np

video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
video.set(10,150)
# 1st green
# abki fazool haa
mycolor= [[20,37,38,174,150,255],
          [0,21,66,129,51,255]
           # [57,76,0,100,255,255],
            #[90,48,0,118,255,255]
            ]
# detectoin sahi nai kr pa ra light ki waja sa..
# code copy kiya haa video sa .
# in values ko theak krna haa

def findColoe(img,mycolor):
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in mycolor:
        lower = np.array(color[0:3])
        higher = np.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, higher)
        #getContours(mask)
        cv2.imshow(str(color),mask)


def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:
            cv2.drawContours(imgresult,cnt,-1,(255,0,0),1)
            # border to mark krna drawcontours sa

            peri = cv2.arcLength(cnt,True)
           # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            obj = len(approx)
            x,y,w,h = cv2.boundingRect(approx)


while True:
    success, img =video.read()
    vid = cv2.resize(img,(400,400))
    imgresult = img.copy()
    findColoe(img,mycolor)

    cv2.imshow("Video Result",imgresult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
       break




#cv2.waitKey(0)
