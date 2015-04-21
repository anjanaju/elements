__author__ = 'anjana'

def findintersection(a, b):
    i=0
    j=0
    l = list()
    while i< len(a) and j< len(b):
        if a[i] == b[j]:
            l.append(a[i])
            i=i+1
            j=j+1
        elif a[i]< b[j]:
            i= i + 1
        else:
            j = j + 1
    return l





a = [1, 3,5,7,9,12, 14]
b = [2, 3, 6, 8, 9, 14, 16]

l = findintersection(a, b)
print(l)
