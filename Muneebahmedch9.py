import cv2
import numpy as np

imgcascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/IMG_8640 (2).JPG")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imggrays = cv2.resize(imggray,(600,300))
#cv2.imshow("gray",imggrays)
# sahi nai show kr ra is ma masla a ra haa... bohat zada
faces = imgcascade.detectMultiScale(imggrays,1.09,4)
for (x,y,w,h) in faces:
   cv2.rectangle(imggrays,(x,y),(x+w,y+h),(0,255,0),3)
   cv2.putText(imggrays, 'Smile', (x + x, y + y), 1, 1, (0, 255, 0), 1)


cv2.imshow("image",imggrays)
cv2.waitKey(0)
