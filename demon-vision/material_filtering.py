import cv2 as cv
import numpy as np
import json
from math import dist
img=cv.imread('testImages/A120roombu.jpg')

def frame_gen(img):
    threshold=12
    height=np.shape(img)[0]
    width=np.shape(img)[1]
    mask = np.full_like(img,0)
    for h in range(1,height-1,1):
        for w in range(1,width-1,1):
            #current color
            pc=img[h,w-1]
            cc=img[h,w]
            dgrad = dist(pc,cc)
            if dgrad>threshold:
                mask[h,w]=255
    for w in range(1,width-1,1):
        for h in range(1,height-1,1):
            #current color
            pc=img[h-1,w]
            cc=img[h,w]
            dgrad = dist(pc,cc)
            if dgrad>threshold:
                mask[h,w]=255
    return mask
frame_mask=frame_gen(img)
cv.imshow('120 roombu',img)
cv.imshow('roombu frame mask',frame_mask)
cv.waitKey(0)