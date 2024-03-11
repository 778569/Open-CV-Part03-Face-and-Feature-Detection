import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)

#Convert this in to gray

gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#this is why? Our classifre not working on color images
#find the path to a XML file
path = "haarcascade_eye.xml"

#making cascade object

eye_cascade = cv2.CascadeClassifier(path)
eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(40,40))
print(len(eyes))

for(x,y,w,h) in eyes:
    xc = (x + x+w)/2
    yc = (y + y+h)/2
    radius = w/2
    cv2.circle(img, (int(xc),int(yc)), int(radius), (255,0,0), 2)
cv2.imshow("Eyes",img)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
