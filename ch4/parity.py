__author__ = 'anjana'

def Parity(x):
    count = 0
    while x>0:
        x = x&(x-1)
        count = count+1
    return count

def initDict():
    d = dict()
    for i in range(0, 16):
        j= Parity(i)
        d[i] = j
    return d

def Calculate(x,d):
    count = 0
    for i in range(1,9):
        y = x & 15
        count = count + d[y]
        x = x >> 4
    return count

d = initDict()
for i in range(0, 16):
    print(i, d[i])
j = Calculate(31, d)
print(j)


