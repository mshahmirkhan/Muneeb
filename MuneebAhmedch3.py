import cv2


# image resize and croping
img = cv2.imread("Resources/image.png")
cv2.imshow("Image ",img)
print(img.shape)
# shape for heigh and width
# app is resized img
# first width then height
app= cv2.resize(img,(300,300))
cv2.imshow("Resized",app)
print(app.shape)

# croping
#first height and then width
crop = img[0:300,0:350]
croped = cv2.imshow("Croped",crop)
cv2.waitKey(0)
