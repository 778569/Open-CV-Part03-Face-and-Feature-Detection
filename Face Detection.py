import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)

#Convert this in to gray

gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#this is why? Our classifre not working on color images
#find the path to a XML file
path = "haarcascade_frontalface_default.xml"

#making cascade object

face_cascade = cv2.CascadeClassifier(path)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(40,40))
print(len(faces))

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # 2- Line thickness

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
