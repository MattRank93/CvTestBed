
import cv2
import absdiff_motiondetection as md
cap = cv2.VideoCapture(0)

md(cap, .02)


# previousFrame = None
# thresh = 1000000
#
#
# def ADP(first, second, thresh):
#     diff = first.copy()
#     cv2.absdiff(first, second, diff)
#     OGvalue = first.sum()
#     value = diff.sum()
#     print(OGvalue)
#     print(value)
#
#     if value > thresh:
#         print("Motion detected")
#     else:
#         print("No motion detected")
#
#     return diff
#
#
# while (cap.isOpened()):
#
#     ret, frame = cap.read()
#
#     if previousFrame is not None:
#         # use previous frame here
#         prev_gray = cv2.cvtColor(previousFrame, cv2.COLOR_BGR2GRAY)
#         # cv2.imshow("previousFrame", prev_gray)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # cv2.imshow("grayframe", gray)
#         apdresult = ADP(gray, prev_gray, thresh)
#         cv2.imshow("apdresult", apdresult)
#         if cv2.waitKey(100) & 0xFF == ord('q'):
#             break
#
#
#     # save current frame
#     previousFrame = frame
#
#
#
#
#
#
#
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
