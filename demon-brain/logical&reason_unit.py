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
    asi = asi.replace(' ','')
    asi = asi.replace('&a:', ' &a: ')
    asi = asi.replace('&r:', ' &r: ')
    asi = asi.replace('&b:', ' &b: ')
    asi = asi.split()
    str_arb_sup(asi)



def str_arb_sup(lsi):
    for i,item in enumerate(lsi):

        print(item)

def is_arb(str):
    return "&a:" in str and "&r:" in str and "&b:" in str

if __name__ == "__main__":
    a = arb(arb('akash','love','saka'),'son','dio')
    strr = arb_str(a)
    str_arb(strr)
