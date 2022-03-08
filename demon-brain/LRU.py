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

    if str(type(data)) =="<class 'str'>":
        aki = str_arb(data)
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
        inv_str_data = arb_str(asi)
    elif "<class '__main__.arb'>":
        aki = data
        str_data = arb_str(data)
        a = aki.a
        r = aki.r
        b = aki.b

        asi = aki
        asi.a, asi.b = asi.b, asi.a
        asi.r = '~' + asi.r
        inv_str_data = arb_str(asi)
        ia = asi.a
        ir = asi.r
        ib = asi.b
        #print(a)
        if is_arb(a):
            #print(a)
            store_arb(a)
        if is_arb(b):
            #print(b)
            store_arb(b)


    with open("C:\\Users\\akash\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json") as f:


        arb_data = json.load(f)
        #storing a
        try:
            arb_data["a"][arb_str(a)].append(str_data)
        except:
            arb_data["a"][arb_str(a)] = [str_data]

        #storing r
        try:
            arb_data["r"][arb_str(r)].append(str_data)
        except:
            arb_data["r"][arb_str(r)] = [str_data]

        #storing b
        try:
            arb_data["b"][arb_str(b)].append(str_data)
        except:
            arb_data["b"][arb_str(b)] = [str_data]

        #inverse relations
        #storing ia
        #print(ia,ir,ib)
        try:
            arb_data["a"][arb_str(ia)].append(inv_str_data)
        except:
            arb_data["a"][arb_str(ia)] = [inv_str_data]

        #storing r
        try:
            arb_data["r"][arb_str(ir)].append(inv_str_data)
        except:
            arb_data["r"][arb_str(ir)] = [inv_str_data]

        #storing b
        try:
            arb_data["b"][arb_str(ib)].append(inv_str_data)
        except:
            arb_data["b"][arb_str(ib)] = [inv_str_data]

    with open("C:\\Users\\akash\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json",'w') as w:
        json.dump(arb_data,w)


def str_arb(asi):
    flag = is_arb(asi)
    asi = asi.replace(' ','')
    asi = asi.replace('&a:', ' &a: ')
    asi = asi.replace('&r:', ' &r: ')
    asi = asi.replace('&b:', ' &b: '
                      )
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


def is_arb(aki):
    if str(type(aki)) == "<class '__main__.arb'>":
        return True
    else:
        return "&a:" in aki and "&r:" in aki and "&b:" in aki

def communicate(sen):
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
        if is_arb(sen):
            store_arb(sen)

def arbDisplay(arr):
    for _,item in enumerate(arr):
        item = item.replace(' ' ,'')
        item = item.replace('&a:', ' ')
        item = item.replace('&r:', ' ' )
        item = item.replace('&b:', ' ')
        print(item)



def retrive(a="_",r="_",b="_"):
    with open("C:\\Users\\akash\\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json") as f:
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

        al = retrive_sup(al)
        rl = retrive_sup(rl)
        bl = retrive_sup(bl)

        #print("al",al)
        #print("rl",rl)
        #print("bl",bl)
        intersection_set = set.intersection(set(al), set(rl),set(bl))
        final_list = list(intersection_set)
        #print(final_list)
        return final_list

def memArbClear():
    cdata = {"a": {}, "r": {}, "b": {}}
    with open("C:\\Users\\akash\PycharmProjects\\Demon's paradise\\demon-brain\\jsonFiles\\memory_arb.json",'w') as w:
        json.dump(cdata,w)

def retrive_sup(aki):
    if str(type(aki))=="<class 'list'>":
        return aki

    else:
        aki = list(aki.values())
        asi = []
        for i in range(len(aki)):
            asi += aki[i]
        return asi

def cTerminal():
    flagcli = True
    while flagcli:
        cmd = str(input ('>>>'))
        if cmd in ['quit','exit','q','e']:
            flagcli = False
        else:
            communicate(cmd)


def DefineRelation():
    """

    description: defines a relation making it easier to retrive information from a sentence

    """
if __name__ == "__main__":
    a = arb(arb('akash','love','saka'),'parent','dio')
    strr = arb_str(a)
    b = arb('akash','love','void')
    store_arb(b)
    v = str_arb(strr)
    retrive(a = "akash",r = "love")

