import cv2
import numpy as np



img = cv2.imread("Resources/playing-cards-png-hd-ace-playing-card-png-2494.png")
imgresize0 = cv2.resize(img ,(300,300))

img1 = cv2.imread("Resources/image.png")
imgresize1 = cv2.resize(img1,(300,300))

imghor0= np.hstack((imgresize0,imgresize1))
imgver= np.vstack((imgresize0,imgresize1))
#imghor1 = cv2.resize(imghor0,(500,500))
cv2.imshow("Horizontal imgages",imghor0)
cv2.imshow("vertical size",imgver)
cv2.waitKey(0)
