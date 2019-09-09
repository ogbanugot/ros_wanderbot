#! /usr/bin/env python2

import cv2
import numpy as np

colors = []

def on_mouse_click (event, x, y, flags, frame):
    if event == cv2.EVENT_LBUTTONUP:
        colors.append(frame[y,x].tolist())

def main():
    # capture = cv2.VideoCapture(0)

    while True:
        frame = cv2.imread("track.png")
        hsv = frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if colors:
            cv2.putText(hsv, str(colors[-1]), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.imshow('frame', hsv)
        cv2.setMouseCallback('frame', on_mouse_click, hsv)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # capture.release()
    cv2.destroyAllWindows()


    minb = min(c[0] for c in colors)
    ming = min(c[1] for c in colors)
    minr = min(c[2] for c in colors)
    maxb = max(c[0] for c in colors)
    maxg = max(c[1] for c in colors)
    maxr = max(c[2] for c in colors)
    
    lb = [minb,ming,minr]
    ub = [maxb,maxg,maxr]
    print lb, ub

if __name__ == "__main__":
    main()