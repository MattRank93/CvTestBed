import string
from datetime import date
import datetime
import cv2
import requests

# api-endpoint
URL = "http://127.0.0.1:5000/MotionDetected"

cap = cv2.VideoCapture(0)


def AbsDiffMd(cap, sensitivity):

    previousFrame = None

    def ADP(first, second, thresh):
        diff = first.copy()
        cv2.absdiff(first, second, diff)
        value = diff.sum()

        print(value)

        if value > thresh:
         print("Motion detected")
         # defining a params dict for the parameters to be sent to the API
         now = datetime.datetime.now()
         PARAMS = {'date': now.strftime("%Y-%m-%d %H:%M:%S")}
         # sending get request and saving the response as response object
         r = requests.post(url=URL, params=PARAMS)
         print(r.status_code)

        else:
         print("No motion detected")

        return diff

    while (cap.isOpened()):

        ret, frame = cap.read()

        base = 10000000





        if previousFrame is not None:
            # use previous frame here
            prev_gray = cv2.cvtColor(previousFrame, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            thresh = (base * sensitivity)
            apdresult = ADP(gray, prev_gray, thresh)
            cv2.imshow("apdresult", apdresult)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

        # save current frame
        previousFrame = frame

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break


AbsDiffMd(cap,0.50)

cap.release()
cv2.destroyAllWindows()
