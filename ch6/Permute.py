__author__ = 'anjana'
a = [5,3,4,2]
b = [3, 1, 0, 2]
c = [0,0,0,0]
for i in range(len(b)):
    c[b[i]] = i
print(c)

for i in range(len(b)):
    j = i
    if c[j] >0 and c[j]!= j:
        temp1 = a[j]
        while c[j] != i:
            temp2 = a[c[j]]
            a[c[j]] = temp1
            c[j] = -c[j]
            j = -c[j]
            temp1 = temp2
            print(a)
            print(c)
        a[c[j]] = temp2
print(a)


