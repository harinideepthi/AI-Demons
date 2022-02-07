import numpy as np
import cv2 as cv
import json
from math import dist

img = cv.imread('testImages/testGold.jpg')
avg=np.mean(np.mean(img,axis=0),axis=0)

with open('jsonFiles/vision.json') as f:
    vis=json.load(f)
    vis["avg"]=avg.tolist()
    print(vis)
    with open('jsonFiles/vision.json','w') as v:
        json.dump(vis,v)



#cv.imshow('testing...',img)
#cv.waitKey(0)
