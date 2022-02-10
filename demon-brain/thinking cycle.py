import json
import random
from classes import *
from functions import *
from character import *
import time


def clock(start_time):
    timer = time.time()- start_time
    return timer
Flag_k= True
Flag_g = True
while Flag_k:
    st= time.time()
    thinking_span = 0.1
    bla = []
    alb=[]
    od=[]
    do=[]
    while clock(st)<thinking_span:
        time.sleep(0.00008)
        with open('jsonFiles/memory_aki.json') as f:
            data = json.load(f)
            bla.append(data[0][random.randint(0,len(data[0])-1)])
        for i in range(len(bla)):
            od.append(decision(actionDs("kaerve", bla[i]), "kaerve" + " " + bla[i], 0))

    final_od = makeDec(od)
    final_obj = final_od.sentence.split(sep= " ")[-1]


    stt= time.time()
    while clock(stt)<thinking_span:

        time.sleep(0.00008)
        with open('jsonFiles/memory_aki.json') as f:
            data = json.load(f)
            alb.append(data[1][random.randint(0, len(data[1]) - 1)])
        for i in range(len(alb)):
            do.append(decision(actionDs(alb[i], final_obj), alb[i] + ' ' + final_obj, 0))

    final_dec = makeDec(do)
    print(final_dec.sentence)
    Flag_k = Flag_g