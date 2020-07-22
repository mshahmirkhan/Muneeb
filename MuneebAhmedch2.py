import cv2
import numpy as np
print("Package imported")
img = cv2.imread("resources/image.png")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
display = cv2.imshow("Image gray",imggray)
#cv2.waitKey(0)


# for img blur
imgblur = cv2.GaussianBlur(imggray, (5,5),0)
display1 = cv2.imshow("Blur gray",imgblur)
# canny krna...
imgcanny = cv2.Canny(img,150,150)
display2 = cv2.imshow("Canny ",imgcanny)

# for egdes idk
kernal = np.ones((5,5),np.uint8)
imgdialation = cv2.dilate (imgcanny,kernal,iterations=1)
display2 = cv2.imshow("Dialation ",imgdialation)

#dialation inverse
imgeroded = cv2.erode(imgdialation,kernal,iterations=1)
display2 = cv2.imshow("Eroded ",imgeroded)

cv2.waitKey(0)
