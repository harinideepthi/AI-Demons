class node:
    def __init__(self, data, pair, operation):
        self.data = data
        self.pair = pair
        self.operation = operation


def calculate(inputt):
    node_type = str(type(inputt))
    if node_type == "<class 'int'>":
        return float(inputt)
    if node_type == "<class 'float'>":
        return inputt
    if node_type == "<class 'str'>":
        inputt = inputt.replace('~','-')
        return float(inputt)
    if node_type == "<class '__main__.node'>":
        data = inputt.data
        pair = inputt.pair
        operation = inputt.operation

        if operation == '+':
            if str(type(data)) or str(type(pair)) =="<class 'str'>":
                return calculate(data) + calculate(pair)
            else:
                return data + pair
        if operation == '-':
            if str(type(data)) or str(type(pair)) =="<class 'str'>":
                return calculate(data) - calculate(pair)
            else:
                return data - pair

        if operation == '*':
            if str(type(data)) or str(type(pair)) =="<class 'str'>":
                return calculate(data) * calculate(pair)
            else:
                return data * pair

        if operation == '/':
            if str(type(data)) or str(type(pair)) =="<class 'str'>":
                return calculate(data) / calculate(pair)
            else:
                return data / pair
        if operation == '^':
            if str(type(data)) or str(type(pair)) =="<class 'str'>":
                return calculate(data) ** calculate(pair)
            else:
                return data ** pair

        if operation == '`':
            if data == 'sin':
                return np.sin(calculate(pair))
            if data =='cos':
                return np.cos(calculate(pair))



def split_operators(input):
    input = input.replace('pi',str(np.pi))
    input = input.replace(' ', '')
    input = input.replace('(',' ( ')
    input = input.replace(')',' ) ')
    input = input.replace('`',' ` ')
    input = input.replace('^',' ^ ')
    input = input.replace('/', ' / ')
    input = input.replace('*', ' * ')
    input = input.replace('+', ' + ')
    input = input.replace('-', ' - ')
    input = input.split()
    return input

def bodmas(input):
    input = split_operators(input)
    #bodmas - brackets
    ebo = 0
    count_o = 0
    count_c = 0
    flag_b = False
    l = len(input)
    for i in range(len(input)):

        if flag_b== False:
            if input[i-ebo]=='(':
                flag_b=True
                o_index = i
        if flag_b:
            if input[i-ebo]=='(':
                count_o+=1
            if input[i-ebo] ==')':
                count_c +=1
            if (count_o - count_c) ==0:
                c_index = i
                t=''
                for i in range(o_index+1,c_index):
                    t += input[i-ebo]
                input[o_index+1-ebo:c_index+1-ebo] = []
                input[o_index-ebo] = bodmas(t)
                ebo = l - len(input)
                flag_b = False
                count_o = 0
                count_c =0
    #bodmas - of
    flag_o = True
    while (flag_o):
        try:
            tdex= input.index('`')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp

        except:
            flag_o = False



    flag_p = True
    while (flag_p):
        try:
            tdex = input.index('^')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp
        except:
            flag_p = False

    #division
    flag_d = True
    while (flag_d):
        try:
            tdex = input.index('/')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp
        except:
            flag_d = False
    #multiplication
    flag_m = True
    while (flag_m):
        try:
            tdex = input.index('*')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp
        except:
            flag_m = False

    flag_a = True
    while (flag_a):
        try:
            tdex = input.index('+')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp
        except:
            flag_a = False

    flag_s = True
    while (flag_s):
        try:
            tdex = input.index('-')
            temp = node(data=input[tdex - 1], operation=input[tdex], pair=input[tdex + 1])
            input[tdex:tdex + 2] = []
            input[tdex - 1] = temp
        except:
            flag_s = False

    return input[0]

def printt(aki):
    if str(type(aki)) == "<class '__main__.node'>":
        return printt(aki.data) + printt(aki.operation) + printt(aki.pair)
    else:
        return str(aki)


ant = bodmas('2/3+3-2*3/4')

