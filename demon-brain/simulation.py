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

diablo = Demon([0, 0, 0], 0, 25)
vision = diablo.vision()
st = time.time()
a=excecute(input=vision,instruction='filod&obj:saod&ptag:100&i:yennt&i:q')
print(vision)
print(a)
def respond(demon,stimulus):
    print(stimulus.object)
    print(stimulus.subject)
    print(stimulus.verb)
    driv=actionDs(stimulus.verb, stimulus.object)
    driv.print()
Tsub= 'subject'
Tobj=objectCombine('palard')
Tver=actionExtractor('moku')
stimuli=asn(subject=Tsub,object=Tobj,verb=Tver)
respond(demon = diablo, stimulus=stimuli)

