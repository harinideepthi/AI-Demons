try:
    from arithmetical_unit import unit
    from functions import *
    from classes import *
    import json

except Exception as e:
    print(e)


class arb:
    """

    a,b - variables
    r - relation

    """
    def __init__(self,a,r,b):
        self.a = a
        self.r = r
        self.b = b

    def print(self):
        print(arb_str(self))

class unit:
        def __init__(self,value, unit):
            self.value = value
            self.unit = unit


def arb_str(aki):
    if str(type(aki))== "<class '__main__.arb'>":
        return "&a:"+arb_str(aki.a)+"&r:"+arb_str(aki.r)+"&b:"+arb_str(aki.b)

    if str(type(aki)) == "<class 'str'>":
        return str(aki)


def store_arb(data):
    with open("C:\\Users\\akash\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json") as f:
        arb_data = json.load(f)
        arb_data.append(data)
    with open("C:\\Users\\akash\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json",'w') as w:
        json.dump(arb_data,w)


def str_arb(asi):
    flag = is_arb(asi)
    asi = asi.replace(' ','')
    asi = asi.replace('&a:', ' &a: ')
    asi = asi.replace('&r:', ' &r: ')
    asi = asi.replace('&b:', ' &b: ')
    asi = asi.split()
    if flag:
        return str_arb_sup(asi)
    else:
        if str(type(asi)=="<class 'list'>"):
            return arr_str(asi)
        else:
            return asi


def str_arb_sup(lsi):
    mt = arb('','','')
    count_a = 0
    count_r = 0
    count_b = 0
    flag_a = False
    flag_r = False
    flag_b = False
    flag_ott1 = True
    flag_ott2 = True
    flag_ott3 = True
    ia = 0
    for i,item in enumerate(lsi):
         if item == '&a:':
              count_a +=1
              #one time trigger function
              if flag_ott1:
                 flag_a = True
                 ia = i
                 flag_ott1 = False

         if item == '&r:':
              count_r += 1
         if item == '&b:':
              count_b +=1
         if flag_a:
             if flag_ott2:
                if count_r-count_a ==0:
                    mt.a = str_arb(arr_str(lsi[ia+1:i]))
                    flag_r = True
                    ir=i
                    flag_ott2 = False
         if flag_r:
             if flag_ott3:
                if count_b-count_r ==0:
                     mt.r = str_arb(arr_str(lsi[ir+1:i]))
                     ib = i
                     flag_b = True
                     flag_ott3 = False

         if flag_b:
            mt.b = str_arb(arr_str(lsi[ib+1:]))
            flag_b = False
    return mt


def arr_str(arr):
    return ' '.join([str(elem) for elem in arr])


def is_arb(str):
    return "&a:" in str and "&r:" in str and "&b:" in str

def communicate(sen):
    if  sen.startswith('&qn:'):
         print("it's a qesution ")

    if sen.startswith('&fact:'):
        if is_arb(sen):
            store_arb(sen)


if __name__ == "__main__":
    a = arb(arb('akash','love','saka'),'son','dio')
    strr = arb_str(a)
    v = str_arb(strr)
