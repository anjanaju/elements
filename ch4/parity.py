__author__ = 'anjana'

def Parity(x):
    count = 0
    while x>0:
        x = x&(x-1)
        count = count+1
    return count%2


y = Parity(11)
print(y)