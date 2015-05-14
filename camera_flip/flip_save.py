#!/usr/bin/env

import numpy as np
import cv2
from pprint import pprint

cap = cv2.VideoCapture(0)

w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('output.mjpg',fourcc, 40.0, (w,h))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()