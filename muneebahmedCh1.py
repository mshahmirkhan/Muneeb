import cv2
print("Package imported")
# read image video and webcam

#img ko import and display
img = cv2.imread("Resources/image.png")
cv2.imshow("output",img)
cv2.waitKey(0)



# video add and display and when press q it ends

cap = cv2.VideoCapture("Resources/FAHD6298.MOV")
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF== ord ('q'):
       break





# webcam open krna ka liya
cap1 = cv2.VideoCapture(0)
# zero or any no means attached cameras or webcame
cap1.set(3,480)
cap1.set(4,360)
cap1.set(10,100)

while True:
    success, img1 = cap1.read()
    cv2.imshow("video",img1)
    if cv2.waitKey(1) & 0xFF== ord ('q'):
        break

# aik aik kr ka chalo to acha haa sub aik sth kam karab kra ga..



