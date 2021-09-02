import string
from datetime import date
import datetime
import cv2
from pip._vendor.requests import *
from requests import *
import requests
import VideoRecorder as VR
# api-endpoint


URL = "http://127.0.0.1:5000/upload"

# cap = cv2.VideoCapture(0)



def AbsDiffMd(cap, sensitivity):

    previousFrame = None

    # def record()

    def ADP(first, second, thresh):
        prev_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
        diff = gray.copy()
        cv2.absdiff(prev_gray, gray, diff)
        value = diff.sum()
        motion = False
        print(value)

        if value > thresh:
            print("Motion detected")
            motion = False
        else:
            print("No motion detected")
            motion = False
        return motion,diff


    while (cap.isOpened()):
        ret, frame = cap.read()
        base = 10000000
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        size = (frame_width, frame_height)
        if previousFrame is not None:
            # use previous frame here
            thresh = (base * sensitivity)
            apdresult = ADP(frame, previousFrame, thresh)
            if apdresult[0] == True:
                result = cv2.VideoWriter('filename.avi',
                                         cv2.VideoWriter_fourcc(*'MJPG'),
                                         10, size)

            cv2.imshow("apdresult", apdresult[1])
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

        # save current frame
        previousFrame = frame

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break



