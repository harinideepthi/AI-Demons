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