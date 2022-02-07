import math
import numpy as np
import scipy.signal as sig

def mod(a):
  return math.sqrt(a[0]**2+a[1]**2)

def dotproduct(a,b):
  return a[0]*b[0]+a[1]*b[1]


def quadrant(origin, cords):
    ox = origin[0]
    oy = origin[1]
    cx = cords[0]
    cy = cords[1]

    if cx <= ox and cy >= oy:
        return 1
    if cx >= ox and cy >= oy:
        return 2
    if cx <= ox and cy <= oy:
        return 3
    if cx >= ox and cy <= oy:
        return 4


def kangle(origin=[0,0],oa=[-1,0],b=[0,0],is_quadratic=True):
  q = quadrant(origin,b)
  #print(q)
  #vector form of -x axis
  #oa =[-1,0]
  #calculating directional vectors oa,ob
  #oa=[a[0]-origin[0],a[1]-origin[1]]
  ob=[b[0]-origin[0],b[1]-origin[1]]
  #finding dot product of two vectors
  dp = dotproduct(oa,ob)
  #finding the angle
  angle= math.acos(dp/(mod(oa)*mod(ob)))
  angle = math.degrees(angle)
  if q>2 and is_quadratic:
    angle = 360-angle

  return angle

def array2bool(a):
    if a[0] and a[1] and a[2]:
        return True
    else:
        return False

def filter(img,clr_le,clr_ue):
    asi=0
    aki=np.zeros([np.shape(img)[0],np.shape(img)[1],1])
    for i in range(np.shape(img)[0]):
        for j in range(np.shape(img)[1]):
            if array2bool(img[i,j]>=clr_le) and array2bool(img[i,j]<=clr_ue):
                aki[i,j] =255
                asi+=1
            else:
                aki[i,j]=0
    return aki,asi
#searching columwise
def frame_gen(img,stepsize=5):
    img = img.copy()
    aki=np.zeros(np.shape(img),'uint8')
    flag=0
    flag_r=0
    cords=[]
    count=0
    cooldown = 10
    for i in range(0,np.shape(img)[1],stepsize):
        for j in range(np.shape(img)[0]):

            if flag == 2:
                count += 1
                # aki[j+1,i] = 0
                if count >= cooldown:
                    count = 0
                    if img[j-1, i] == 0:
                        flag = 0
                    if img[j-1, i] == 255:
                        flag = 1
            if flag==0:
                if img[j,i]==255:
                   aki[j,i] = 255
                   cords.append([j,i])
                   flag=2

            if flag==1:
                if img[j,i]==0:
                    aki[j-1, i] = 255
                    cords.append([j-1,i])
                    flag = 2


    for i in range(0,np.shape(img)[0],stepsize):
        for j in range(np.shape(img)[1]):

            if flag_r==2:
                count +=1
                #aki[i+1,j]=0
                if count>=cooldown:
                    count=0
                    if img[i-1,j]==0:
                        flag_r =0
                    if img[i-1, j]==255:
                        flag_r = 1

            if flag_r==0:

                if img[i,j]==255:
                    aki[i,j]=255
                    cords.append([i,j])
                    flag_r=2

            if flag_r==1:
                if img[i,j]==0:
                    aki[i-1,j] =255
                    cords.append([i-1,j])
                    flag_r=2


    return aki,cords

def nosides(grf):
    grf = grf+grf
    a = sig.find_peaks(grf, width=2, distance=2)
    l = len(a[0])
    if l%2==1:
        return (l+1)/2
    else:
        return l
