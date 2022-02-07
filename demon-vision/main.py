import cv2 as cv
import numpy as np
from math import dist
import time
import math
import matplotlib
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import scipy.signal as sig
from functions import *
import sys
from sklearn.preprocessing import MinMaxScaler


mm_scaler = MinMaxScaler()
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


st=time.time()


class point:
    def __init__(self,point,angle,distance):
        self.point=point
        self.angle = angle
        self.distance = distance

lower_limit = (67,167,25)
upper_limit = (87,187,45)


#reading the image
aki = cv.imread("testImages/testGreenCircle.jpg", cv.IMREAD_COLOR)
#cv.imshow('originalimage',aki)
aki = cv.inRange(aki,lower_limit,upper_limit )

# print(asi)
cv.imshow('greemask',aki)
fsd = time.time()

asi, cord = frame_gen(aki,stepsize=1)
cord = np.array(cord)
cord=np.unique(cord,axis=0)

max=np.max(cord,axis=0)
min=np.min(cord,axis=0)

points=[]
center=[(max[0]+min[0])/2,(max[1]+min[1])/2]

def test(frame, sp, memo, sz=7):
    memo.append(1)
    global mi
    global mj
    global mdistt
    mdistt=500
    mi=0
    mj=0

    for i in range(sp[0]-sz,sp[0]+sz,1):
        for j in range(sp[1]-sz,sp[1]+sz,1):

            if frame[i,j]==255:
                distt = dist([sp[0], sp[1]], [i, j])

                if distt:
                    if distt<mdistt:
                        mdistt = mdistt
                        memo.pop()
                        frame[mi,mj]=255
                        mi=i
                        mj=j
                        frame[mi,mj]=22
                        memo.append([mi,mj])

    if frame[mi,mj]==22:
        test(frame, [mi, mj],memo=memo)
    return memo


lsi = asi.copy()
cord = test(lsi,cord[0],memo=[])
cord.pop()

for i in cord:
    points.append(point(i, kangle(center, i), dist(center, i)))


dis = []

for i in points:
    dis.append([i.distance])

dis = np.array(dis)
lti = np.linspace( 0,100,len(cord) )
# dis = mm_scaler.fit_transform(dis)

esi=plt.plot(lti,dis)


dis = np.array(dis)
dis = np.reshape(dis,len(dis))
print(dis)
nofsides=nosides(dis)

print(nofsides)

if nofsides==4:
    print("it's a square")
if nofsides==5:
    print("it's a pentagon")
if nofsides==6:
    print("it's a hexagon")


print(cord)
cv.imshow('squareframe',asi)
cv.imshow('processed frame',lsi)


print(time.time()-st)



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
