import cv2
import numpy
import numpy as np
print("********package imported")
# "// ading image
# imgeraeder = cv2.imread('resorces/6n.png')
# cv2.imshow('output',imgeraeder)
# cv2.waitKey(10000),print("********done")

# addiifn videos
# VideoCapture = cv2.VideoCapture("resorces/videos/12.mp4")
# while True:
#     sucessfull,snip=VideoCapture.read()
#     cv2.imshow("VideoCa",snip)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# addiifn    videos
# WebcamCapture = cv2.VideoCapture(0)
# WebcamCapture.set(3,640)
# WebcamCapture.set(4,480)
#

# # brigness
# WebcamCapture.set(10,100)
# while True:
#     sucessfull, snip = WebcamCapture.read()
#     cv2.imshow("VideoCa", snip)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


#converting to grayscale

Kernel= np.ones((5,5),np.uint8)
imgeraeder = cv2.imread('resorces/6n.png')
imgGrayScale =cv2.cvtColor(imgeraeder,cv2.COLOR_BGR2GRAY)
imgBlur =cv2.GaussianBlur(imgGrayScale,(7,7),0)
# edged detector
imgEdge = cv2.Canny(imgGrayScale,15,10)

# dilation
imgeDiltion = cv2.dilate(imgEdge,Kernel,iterations=1)


cv2.imshow('output',imgGrayScale)
cv2.imshow('output2',imgeDiltion)
cv2.imshow('output3',imgEdge)



cv2.waitKey(10000),print("********done")
