try:
    from math import dist
    import json
    import random
    from classes import *
    from functions import *
    from character import *
    from demon import *
    import numpy as np
    import cmath
    import matplotlib.pyplot as plt
    from numpy import sin,cos,tan
    from mpl_toolkits import mplot3d
except Exception as e:
    print(f'error importing : {e} ')

# diablo = Demon([0, 0, 0], 0, 25)
# vision = diablo.vision()
#st = time.time()
#a=excecute(input=vision,instruction='filod&obj:saod&ptag:100&i:yennt&i:q')
#print(vision)
#print(a)
# def respond(demon,stimulus):
#     print(stimulus.object)
#     print(stimulus.subject)
#     print(stimulus.verb)
#     driv=action_ds(stimulus.verb,stimulus.object)
#     driv.print()
# Tsub= 'subject'
# Tobj=object_obj('palard')
# Tver=action_extractor('moku')
# stimuli=asn(subject=Tsub,object=Tobj,verb=Tver)
# respond(demon = diablo, stimulus=stimuli)

class unit:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit


class formula:
    def __init__(self,requirements,input,formula):
        self.requirements = requirements
        self.input = input
        self.formula = formula
    def print(self):
        print(f'requirements:{self.requirements}')
        print(f'input: {self.input}')
        print(f'formula: {self.formula}')
    def calculate(self,to_find):
        print('tofind')

        print('fdkj')

def find_roots(x,y):
    s = np.abs(np.diff(np.sign(y))).astype(bool)
    print(s)
    return x[:-1][s] + np.diff(x)[s]/(np.abs(y[1:][s]/y[:-1][s])+1)

def generate(signal,variable,lower_limit,upper_limit,sampling_rate=10):
    x = np.linspace(lower_limit,upper_limit, (upper_limit - lower_limit) *sampling_rate)
    #print(x)
    y  = []
    yr = []
    yi = []
    signal = signal.replace(variable,'z')
    for i in x:
        for j in x:
            z= complex(i,j)
            temp = eval(signal)
            y.append(temp)
            yr.append(temp.real)
            yi.append(temp.imag)
    return x,np.array(yr),np.array(yi)

requirement = ['force','mass','acceleration']
inpu = {'mass': 12, 'accelaration': 0.5}
form = 'force-mass*accelaration'
tlo = formula(requirement,inpu,form)

x,yr,yi = generate('x**2-2*x+4','x',-20,20,10)
print(yi)

ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(x, yr, yi, 'gray')


plt.show()