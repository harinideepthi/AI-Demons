import cv2 as cv
import numpy as np
import json

#source light values
source =(255,255,255)

img=cv.imread('testImages/testGold.jpg')
shape=np.shape(img)
div=shape[0]*shape[1]

with open('jsonFiles/vision.json') as f:
    vis=json.load(f)
    avg=vis["avg"]

paddingCoef=0.1
padding=paddingCoef*((source[0]-avg[0])+(source[1]-avg[1])+(source[2]-avg[2]))/3
print(padding)
print(f'avg color {avg[0],avg[1],avg[2]}')

PavgPVB=avg[0]+padding
if PavgPVB>255:
    PavgPVB=255

PavgPVR=avg[2]+padding
if PavgPVR>255:
    PavgPVR=255

PavgPVG=avg[1]+padding
if PavgPVG>255:
    PavgPVG=255

mask=cv.inRange(img,(PavgPVR,PavgPVG,PavgPVB),(255,255,255))

#wpix- white pixels
wpix = np.argwhere(mask == 255)
aki=np.shape(wpix)[0]
#white gradient
wgrad=np.array([0,0,0])
for i in wpix:
    wgrad+=img[i[0],i[1]]
print(f'wgrad {wgrad/aki}')

spix = np.argwhere(mask == 0)
asi=np.shape(wpix)[0]

#white gradient
sgrad=np.array([0,0,0])
for i in spix:
    sgrad+=img[i[0],i[1]]
    pass
print(f'sgrad {sgrad/asi}')

#metalic nature
Mnat=aki/div
#
cv.imshow('OGimg',img)
cv.imshow('mask',mask)
cv.waitKey(0)
cv.destroyAllWindows()