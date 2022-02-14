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

class unit:

    """

    description: class: used to denote a value with a unit
    parameter: value, unit

    """

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
    return x[:-1][s] + np.diff(x)[s]/(np.abs(y[1:][s]/y[:-1][s])+1)

def generate(signal,variable,lower_limit,upper_limit,sampling_rate=10):
    x = np.linspace(lower_limit,upper_limit, (upper_limit - lower_limit) *sampling_rate)
    #print(x)
    y = []
    for i in x:
        temp = eval(signal)
        y.append(temp)
    return x,np.array(y)

if __name__ == '__main__':
    requirement = ['force','mass','acceleration']
    inpu = {'mass': 12, 'accelaration': 0.5}
    form = 'force-mass*accelaration'
    tlo = formula(requirement,inpu,form)


    x,y = generate('x**2-2*x+4','x',-20,20,10)
    print(x,y)
    #print(y)
    z = find_roots(x,y)
    plt.show(x,y)
    plt.show()


    find_roots(x,y)