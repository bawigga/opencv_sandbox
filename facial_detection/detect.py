import numpy as np
import cv2
from pprint import pprint

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

cam.set(3,640)
cam.set(4,480)

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret==True:
        # frame = cv2.flip(frame,0)

        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()