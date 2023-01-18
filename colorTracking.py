import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while(True):
    __, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerBlue = np.array([110, 50, 50])
    higherBlue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lowerBlue, higherBlue)

    th = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,27,2)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    contours, __ = cv2.findContours(~th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for __,contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 500):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y), (x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('threshold',th)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()