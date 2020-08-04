# document Scanner
import cv2
import numpy as np
import requests



url = ("http://192.168.10.2:8080/shot.jpg")
#cap1 = cv2.VideoCapture(0)
# zero or any no means attached cameras or webcame



def preProcessing(img):
     img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     img_blur = cv2.GaussianBlur(img_gray,(5,5),1)
     img_canny = cv2.Canny(img_blur,200,200)
     kernal = np.ones((5,5))
     img_dial = cv2.dilate(img_canny,kernal,iterations=2 )
     img_thrushold = cv2.erode(img_dial,kernal,iterations=1)
     return img_thrushold


def getContours(img):
    Biggest = np.array([])
    maxarea = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>5000:
            cv2.drawContours(imgcon,cnt,-1,(255,0,0),20)
            # border to mark krna drawcontours sa
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(approx)
            if area > maxarea and len(approx) == 4:
                Biggest = approx
                maxarea = area
            #print("hello",len(approx))
            #obj = len(approx)
            #x,y,w,h = cv2.boundingRect(approx)

    return Biggest
def reorder(points):
    points = points.reshape((4,2))
    points_new = np.zeros((4,1,2),np.int32)
    add = points.sum(1)
    #print ("add",add)

    points_new[0] = points [np.argmin(add)]
    points_new[3] = points [np.argmax(add)]

    diff = np.diff(points,axis=1)
    points_new[1] = points [np.argmin(diff)]
    points_new[2] = points[np.argmax(diff)]
    #print("New Points ", points_new)
    return points_new

def getWrap(img,Biggest):
    Biggest = reorder(Biggest)
    print("fuckde",Biggest.shape)
    pts1 = np.float32(Biggest)
    pts2 = np.float32([[0, 0], [widthimg, 0], [0, heightimg], [widthimg, heightimg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgoutput= cv2.warpPerspective(img, matrix, (widthimg, heightimg))
    return imgoutput

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

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), np.uint8)
    img1 = cv2.imdecode(img_arr,-1)
    #success, img1 = cap1.read()
    widthimg = 640
    heightimg = 360
    img = cv2.resize(img1,(widthimg,heightimg))
    imgcon = img.copy()
    img_thrushold = preProcessing(img)
    Biggest = getContours(img_thrushold)
    print(Biggest.shape)
    print ("add")
    reorder(Biggest)
    img_Wraped = getWrap(img,Biggest)
    img_array = ([img,imgcon],
                 [img_thrushold,img_Wraped])
    stack = stackImages(0.6,img_array)
    cv2.imshow("video",stack)
    if cv2.waitKey(1) & 0xFF== ord ('q'):
        break
