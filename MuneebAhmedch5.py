import  cv2
import numpy as np

# img ko crop krna points ka lahaz saa ... charo corners saa..
img = cv2.imread("Resources/playing-cards-png-hd-ace-playing-card-png-2494.png")
img1 = cv2.resize(img,(500,500))

width , height = 250,300

pts1 = np.float32([[1329,129],[2453,441],[887,1713],[2053,2023]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))
#print (img1.shape)
cv2.imshow("card",img1)
cv2.imshow("card pic",imgoutput)
print (img.shape)








cv2.waitKey(0)
