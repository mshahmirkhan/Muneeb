#text and color
import cv2
import numpy as np

img = np.zeros((512,512,3))
print (img.shape)
# 255 means blue
img[:] = 255,0,0
cv2.imshow("image blue ",img)
#255,255,255 means white
img[:] = 255, 255, 255
#cv2.imshow("image", img)


# line on image
app =cv2.line(img,(0,0),(img.shape[1],img.shape[1]),(0,255,0),3)
#cv2.imshow("line image",app)
# same for rectangle first img name, start point, end point, color of line,thickness
#instead of thickness we can fill the rectangel by cv2.FILLED (capital lettters) in place of thickness (2)
rect = cv2.rectangle(img,(0,0),(250,250),(255,255,0),2)
#cv2.imshow("rect",rect)
circle = cv2.circle(img,(250,250),100,(0,0,128),4)
#cv2.imshow("circle",circle)

# for writing text in image
text =cv2.putText(img,"OPENCV homies",(0,400),cv2.FONT_ITALIC,1,(0,0,215),5)
cv2.imshow("Text image",text)
cv2.waitKey(0)
