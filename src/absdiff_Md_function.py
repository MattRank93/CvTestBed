
import cv2

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
        else:
         print("No motion detected")

        return diff

    while (cap.isOpened()):

        ret, frame = cap.read()




        if previousFrame is not None:
            # use previous frame here
            prev_gray = cv2.cvtColor(previousFrame, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            thresh = (gray.sum() * sensitivity)
            apdresult = ADP(gray, prev_gray, thresh)
            cv2.imshow("apdresult", apdresult)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

        # save current frame
        previousFrame = frame

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break


AbsDiffMd(cap,0.04)

cap.release()
cv2.destroyAllWindows()
