
import cv2
import absdiff_motiondetection as md


cap = cv2.VideoCapture(0)

md.AbsDiffMd(cap, .02)


