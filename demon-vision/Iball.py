#import panunga frand
try:
    import cv2 as cv
    import numpy as np
    import math
    from test import *
    from matplotlib import pyplot as plt
except Exception as e:
    print(f'exception is : {e}')
#main
#fdl --- focus domain length, vis -- wt is see img
class Iball:
    def __init__(self,pos,fdl,vis):
        self.pos=pos
        self.fdl = fdl
        self.vis = vis


img = cv.imread('testImages//bla.jpg')
aki = Iball ([250,250],10,img)
print(f'size: {np.shape(img)}')
# do some shit idk bruh
def Idomain(aki):
    a=[]
    a.append(aki.vis.shape[0]-aki.pos[0]-aki.fdl)
    a.append(aki.pos[1]-aki.fdl)
    a.append(aki.pos[0]-aki.fdl)
    a.append(aki.vis.shape[1]-aki.pos[1]-aki.fdl)
    return a
#ripple creation

def ripple_generation(distance,lower_limit,upper_limit,increment):
    i=lower_limit
    ret=[]
    dis=0
    while dis<=distance:
        ret.append(i)
        dis+=i
        if i<upper_limit:
            i+=increment

    if dis>distance:
        temp=dis-distance
        ret[-1]=ret[-1]-temp
        if ret[-1]==0:
            ret.pop()

    return ret
def ripple_bool(it,target,error_tolerance,flag):
    #x is const, y is var
    if flag==1:
        for i in range(it[0][1],it[1][1],1):
            print(i)
            if math.dist(img[it[0][0]-1,i-1],target)<=error_tolerance:
                return True
        return False
    #y is const, x is var
    if flag==2:
        for i in range(it[0][0],it[1][0],1):
            if math.dist(img[i,it[0][1]],target)<=error_tolerance:
                return True
        return False

    if flag==3:
        for i in range(it[0][1],it[1][1],1):
            if math.dist(img[it[0][0],i],target)<=error_tolerance:
                return True
        return False
    #y is const, x is var
    if flag==4:
        for i in range(it[0][0],it[1][0],1):
            if math.dist(img[i,it[0][1]],target)<=error_tolerance:
                return True
        return False

def ripple_itgen(o,fdl,r,shape,flag):
    x=o[0]
    y=o[1]
    z=fdl+r
    xa=x+z
    xs=x-z
    ya=y+z
    ys=y-z
    xmax=shape[0]-1
    ymax=shape[1]-1
    if xa>xmax:
        xa=xmax
    if ya>ymax:
        ya=ymax
    if xs<0:
        xs=0
    if ys<0:
        ys=0

    if flag==1:
        return [[xa,ys],[xa,ya]]
    if flag==2:
        return [[xs,ys],[xa,ys]]
    if flag==3:
        return [[xs,ys],[xs,ya]]
    if flag==4:
        return [[xs,ya],[xa,ya]]


rip=Idomain(aki)
print(rip)
git=[]
for i in range(4):
    ripple=ripple_generation(rip[i],lower_limit=2,upper_limit=10,increment=2)
    print(ripple)
    jj=0
    inc=0
    flag=True
    while flag:

        j=ripple[inc]
        jj+=j

        it=ripple_itgen(o=aki.pos,r=jj,fdl=aki.fdl,shape=np.shape(img),flag=i+1)
        print(it)
        print(f'flag {i+1}')
        asi=ripple_bool(it,target=img[250,250],error_tolerance=10,flag=i+1)
        inc+=1
        if asi==False:
            git.append(jj)
            flag=False

        print(asi)
        if inc > len(ripple):
            git.append(j)
            flag=False

print(f'git: {git}')
et=10

sp=(aki.pos[0]-git[1]-aki.fdl-et,aki.pos[1]-git[2]-aki.fdl-et)
ep=(aki.pos[0]+git[3]+aki.fdl+et,aki.pos[1]+git[0]+aki.fdl+et)
print(f'sp,ep = {sp,ep}')
#mask=img.copy()
cv.rectangle(img,sp,ep,(0,0,255),2)
mask=img[sp[1]:ep[1],sp[0]:ep[0]]

lower_limit = (67,167,25)
upper_limit = (87,187,45)
gim,y,diz=kat(img=mask,lower_limit=lower_limit,upper_limit=upper_limit)
print('akdfjlaj')



cv.imshow("original image",img)
cv.imshow('mask',mask)
plt.plot(y,diz)
plt.show()
cv.waitKey(0)