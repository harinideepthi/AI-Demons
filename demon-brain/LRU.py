try:
    from ARU import unit
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
        print(arbToStr(self))

class unit:
        """

        value
        unit

        """

        def __init__(self,value, unit):
            self.value = value
            self.unit = unit


def arbToStr(aki):
    """

    parameter: aki
    description: converts an arb class to a string class
    returns: asi

    """
    if str(type(aki))== "<class '__main__.arb'>":
        return "&a:" + arbToStr(aki.a) + "&r:" + arbToStr(aki.r) + "&b:" + arbToStr(aki.b)

    if str(type(aki)) == "<class 'str'>":
        return str(aki)


def storeArb(data):

    """

    parameters: data
    description: stores arb in json file
    returns:

    """

    if str(type(data)) =="<class 'str'>":
        aki = strToArb(data)
        str_data = data
        a = aki.a
        r = aki.r
        b = aki.b
        asi = aki
        asi.a, asi.b = asi.b, asi.a
        asi.r = '~' + asi.r
        ia = asi.a
        ir = asi.r
        ib = asi.b
        inv_str_data = arbToStr(asi)
    elif "<class '__main__.arb'>":
        aki = data
        str_data = arbToStr(data)
        a = aki.a
        r = aki.r
        b = aki.b

        asi = aki
        asi.a, asi.b = asi.b, asi.a
        asi.r = '~' + asi.r
        inv_str_data = arbToStr(asi)
        ia = asi.a
        ir = asi.r
        ib = asi.b
        #print(a)
        if isArb(a):
            #print(a)
            storeArb(a)
        if isArb(b):
            #print(b)
            storeArb(b)


    with open("jsonFiles/memory_arb.json") as f:


        arb_data = json.load(f)
        #storing a
        try:
            arb_data["a"][arbToStr(a)].append(str_data)
        except:
            arb_data["a"][arbToStr(a)] = [str_data]

        #storing r
        try:
            arb_data["r"][arbToStr(r)].append(str_data)
        except:
            arb_data["r"][arbToStr(r)] = [str_data]

        #storing b
        try:
            arb_data["b"][arbToStr(b)].append(str_data)
        except:
            arb_data["b"][arbToStr(b)] = [str_data]

        #inverse relations
        #storing ia
        #print(ia,ir,ib)
        try:
            arb_data["a"][arbToStr(ia)].append(inv_str_data)
        except:
            arb_data["a"][arbToStr(ia)] = [inv_str_data]

        #storing r
        try:
            arb_data["r"][arbToStr(ir)].append(inv_str_data)
        except:
            arb_data["r"][arbToStr(ir)] = [inv_str_data]

        #storing b
        try:
            arb_data["b"][arbToStr(ib)].append(inv_str_data)
        except:
            arb_data["b"][arbToStr(ib)] = [inv_str_data]

    with open("jsonFiles/memory_arb.json",'w') as w:
        json.dump(arb_data,w)


def strToArb(asi):

    """

    parameters: asi
    description: converts string to arb class if it is a convertabel
    returns: lsi

    """

    flag = isArb(asi)
    asi = asi.replace(' ','')
    asi = asi.replace('&a:', ' &a: ')
    asi = asi.replace('&r:', ' &r: ')
    asi = asi.replace('&b:', ' &b: '
                      )
    asi = asi.split()
    if flag:
        return strToArbSup(asi)
    else:
        if str(type(asi)=="<class 'list'>"):
            return arrToStr(asi)
        else:
            return asi


def strToArbSup(lsi):

    """

    support function for strToArb function

    """

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
                    mt.a = strToArb(arrToStr(lsi[ia + 1:i]))
                    flag_r = True
                    ir=i
                    flag_ott2 = False
         if flag_r:
             if flag_ott3:
                if count_b-count_r ==0:
                     mt.r = strToArb(arrToStr(lsi[ir + 1:i]))
                     ib = i
                     flag_b = True
                     flag_ott3 = False

         if flag_b:
            mt.b = strToArb(arrToStr(lsi[ib + 1:]))
            flag_b = False
    return mt


def arrToStr(arr):

    """

    parameters: arr
    description: converts array to string
    returns: str

    """
    return ' '.join([str(elem) for elem in arr])


def isArb(aki):

    """

    parameters: aki
    description: checks if the give input is arb class or arb convertable
    returns: bool

    """

    if str(type(aki)) == "<class '__main__.arb'>":
        return True
    else:
        return "&a:" in aki and "&r:" in aki and "&b:" in aki

def communicate(sen):

    """

    parameters: sen
    description: communicates with the AI / demon
    returns: NULL

    """

    if  sen.startswith('&qn:'):
        nen = sen
        nen = nen.replace('&qn:','')
        nen = nen.replace(' ','')
        nen = nen.replace('&a:',' ')
        nen = nen.replace('&r:', ' ')
        nen = nen.replace('&b:', ' ')
        nen = nen.split()
        data = retrive(*nen)
        arbDisplay(data)
    if sen.startswith('&fact:'):
        sen = sen.replace(' ','')
        sen = sen.replace('&fact:','')
        if isArb(sen):
            storeArb(sen)

def arbDisplay(arr):

    """

    parameters: arr
    description: displays the arb to aprropriate sentence
    returns: NULL

    """

    for _,item in enumerate(arr):
        item = item.replace(' ' ,'')
        item = item.replace('&a:', ' ')
        item = item.replace('&r:', ' ' )
        item = item.replace('&b:', ' ')
        print(item)



def retrive(a="_",r="_",b="_"):

    """

    parameters: a,r,b
    description: retrive the data stored from memory by the specific
    returns: final_list

    """

    with open("jsonFiles/memory_arb.json") as f:
        data = json.load(f)
        #a
        if a == "_":
            al = data["a"]
        else:
            al = data["a"][a]

        if r == "_":
            rl = data["r"]
        else:
            rl = data["r"][r]

        if b == "_":
            bl = data["b"]
        else:
            bl = data["b"][b]

        al = retriveSup(al)
        rl = retriveSup(rl)
        bl = retriveSup(bl)

        #print("al",al)
        #print("rl",rl)
        #print("bl",bl)
        intersection_set = set.intersection(set(al), set(rl),set(bl))
        final_list = list(intersection_set)
        #print(final_list)
        return final_list

def memArbClear():

    """

    description: clears / resets memory_arb with default parameters

    """

    cdata = {"a": {}, "r": {}, "b": {}}
    with open("jsonFiles/memory_arb.json",'w') as w:
        json.dump(cdata,w)

def retriveSup(aki):

    """

    support function to retrive function

    """
    if str(type(aki))=="<class 'list'>":
        return aki

    else:
        aki = list(aki.values())
        asi = []
        for i in range(len(aki)):
            asi += aki[i]
        return asi

def cTerminal():

    """

    description: starts a communication terminal for us to communicate

    """

    flagcli = True
    while flagcli:
        cmd = str(input ('>>>'))
        if cmd in ['quit','exit','q','e']:
            flagcli = False
        else:
            communicate(cmd)


def DefineRelation(relation, sen):
    """

    description: defines a relation making it easier to retrive information from a sentence

    """
    with open('jsonFiles/mem_rdef.json') as f:
        data = json.load(f)
        try:
            data["relation"][relation].append(sen)
        except:
            data["relation"][relation] = [sen]
    with open('jsonFiles/mem_rdef.json','w') as w:
        json.dump(data,w)

def infoTranslate(arb):
    """

    param: sen(str)
    description: unravels a sentence and extracts all information possible/given and returns as a list of data
    returns: data(list)

    """
    arb = strToArb(arb)
    a = arb.a
    r = arb.r
    b = arb.b


    with open('jsonFiles/mem_rdef.json') as f:
        data = json.load(f)
    data = data['relation'] [r]
    for i,item in enumerate(data):
        item = item.replace('#a',a)
        item = item.replace('#r',r)
        data[i] = item.replace('#b',b)

    return data

#logical relation formula
def storeLRF(lrf):
    with open('jsonFiles/mem_lrf.json') as f:
        data = json.load(f)


def solveLogicalRelation(str):
    print(str)


if __name__ == "__main__":
    a = arb(arb('akash','love','saka'),'parent','dio')
    strr = arbToStr(a)
    b = arb('akash','love','void')
    storeArb(b)
    v = strToArb(strr)
    retrive(a = "akash",r = "love")

