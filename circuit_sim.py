def OR(a,b):
    if a or b == True:
        return 1
    else:
        return 0
def AND(a,b):
    if a and b == True:
        return 1
    else:
        return 0
def XOR(a,b):
    if a and b == True:
        return 0
    elif a or b == True:
        return 1
    else:
        return 0
def NAND(a,b):
    if not AND(a,b):
        return 1
    else:
        return 0
def NOR(a,b):
    if a and b == 0:
        return 0
    else:
        return 1
def NOT(a):
    if a == 1:
        return False
    else:
        return True

def half_adder(a,b):
    s = XOR(a,b)
    c = AND(a,b)

    return (s,c)
def half_subtract(a,b):
    s = XOR(a,b)
    c = AND(NOT(a),b)
    return(s,c)

def full_adder(a,b,cin):
    node1 = half_adder(a,b)
    x = node1[0]
    y = node1[1]
    node2 = half_adder(x,cin)
    x2 = node2[0]
    y2 = node2[1]

    y3 = OR(y2,y)
    return (y3,x2)

def full_subtractor(a,b,cin):
    node1 = half_subtract(a,b)
    x = node1[0]
    y = node1[1]
    node2 = half_subtract(x,cin)
    x2 = node2[0]
    y2 = node2[1]

    y3 = OR(y2,y)
    return (x2,y3)


def clean(bit_array):
    x = map(str,bit_array)
    x = ''.join(x)
    return int(x)
        

def convertToBit(bit,n):
    num = bin(n)
    num = list(num)
    num.pop(0)
    num.pop(0)
    num = map(int,num)
    zeros = bit - len(num)
    zero_array = []
    for i in range(zeros):
        zero_array.append(0)
    bin_array = zero_array + num
    return bin_array

def convertToInt(bit):
    return int(str(bit), 2)

def reverse_array(n):
    new = []
    for i in range(len(n), 0,-1):
        new.append(n[i - 1])
    return new

def addByBit(bit,a,b):
    a = convertToBit(bit,a)
    b = convertToBit(bit,b)
    node = half_adder(a[bit - 1],b[bit - 1])
    output = []
    output.append(node[0])
    cin = node[1]

    for i in range(bit-2,-1,-1):
        node = full_adder(a[i],b[i],cin)
        s = node[1]
        c = node[0]
        output.append(s)
        cin = c
    return clean(reverse_array(output))
    
def subByBit(bit,a,b):
    a = convertToBit(bit,a)
    b = convertToBit(bit,b)
    node = half_adder(a[bit - 1],b[bit - 1])
    output = []
    output.append(node[0])
    cin = node[1]

    for i in range(bit-2,-1,-1):
        node = full_adder(a[i],XOR(1,b[i]),cin)
        s = node[1]
        c = node[0]
        output.append(s)
        cin = c
    return clean(reverse_array(output))

def multiplyByBit(bit,a,b):
    num = 0
    if a < b:
        for i in range(a):
            num = convertToInt(addByBit(bit,num,b))
    else:
        for i in range(b):
            num = convertToInt(addByBit(bit,num,a))
    return clean(convertToBit(bit,num))

def divideByBit(bit,a,b):
    count = 0
    for i in range(a):
        if convertToInt(multiplyByBit(bit,i,b)) < a:
            count = convertToInt(addByBit(bit,1,count))
        else:
            return count
            
        
