import numpy as np
import cv2
from matplotlib import pyplot as plt
#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(1)
imgL = cv2.imread('tsukuba_l.png',0)
imgR = cv2.imread('tsukuba_r.png',0)
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()