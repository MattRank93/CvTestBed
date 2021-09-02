
import cv2
import absdiff_motiondetection as amd
import absdiff_record_send as ars


cap = cv2.VideoCapture(0)


# amd.AbsDiffMd(cap, .10)


ars.AbsDiffMd(cap, .10)


