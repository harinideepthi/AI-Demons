import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt
from functions import *
import time

class point_pda:
    def __init__(self,point,distance,angle,derites):
        self.point=point
        self.distance=distance
        self.angle=angle
        self.derites = derites

def dec_nsp(trupoi):
    poi=[]
    for i in trupoi:
        if i.angle<=180:
            poi.append(i)
    poi.sort(key=lambda x: x.distance)
    return poi[-1]

def frame_path_gen(frame,starting_point):
    flag=True
    standing_node=starting_point
    poi=[starting_point]
    domain=1
    frame[standing_node.point[0],standing_node.point[1]]=255
    count=0
    vis_poi = [1, 1]
    while flag:
        trupoi=[]

        for i in range(standing_node.point[0] - domain, standing_node.point[0] + domain, 1):
            for j in range(standing_node.point[1] - domain, standing_node.point[1] + domain, 1):
                if frame[i,j]==255:
                    temp = math.dist(standing_node.point,[i,j])
                    if temp:
                        trupoi.append( point_pda([i,j],temp, kangle(origin=standing_node.point, oa=vis_poi ,b=[i,j], is_quadratic=False),derites=0))

        try:
            # count+=1
            # if count==900:
            #     flag=False

            standing_node = dec_nsp(trupoi=trupoi)
            frame[standing_node.point[0],standing_node.point[1]]=0

            if standing_node.point==starting_point.point:
                flag=False
            poi.append(standing_node)
            domain=1
            vis_poi=[poi[-1].point[0] - poi[-2].point[0] ,poi[-1].point[1]  - poi[-2].point[1] ]
        except:
            domain+=1
    return poi


def kat(img,lower_limit,upper_limit):
    print('adei')
    asi = cv.inRange(img, lowerb=lower_limit, upperb=upper_limit)
    frame,cord = frame_gen(asi,stepsize=1)
    max=np.max(cord,axis=0)
    min=np.min(cord,axis=0)
    center=[(max[0]+min[0])/2,(max[1]+min[1])/2]
    flag_f=True
    si=0
    while flag_f:
        img =frame_path_gen(frame=frame,starting_point= point_pda(cord[si],distance=0,angle=0,derites=0))
        if len(img)<50:
            si+=10
        else:
            si=0
            flag_f=False
    diz=[]
    print('ina thala')
    for i in img:
        diz.append(math.dist(center,i.point))
    y=np.linspace(0,50,len(diz))
    return img,y,diz


lower_limit = (67,167,25)
upper_limit = (87,187,45)
temp=time.time()
aki = cv.imread('testImages/testGreenHexagon.jpg')
print(np.shape(aki))
dim=(236,322)
#aki = cv.resize(aki, dim, interpolation = cv.INTER_AREA)
# img,y,diz=kat(img=aki,lower_limit=lower_limit,upper_limit=upper_limit)
# print(time.time()-temp)
# plt.plot(y,diz)
# plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()