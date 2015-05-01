__author__ = 'anjana'
a = [1, 2, 3, 4, 5, 6]
c = 3
if len(a)% c != 0:
    k = 1
    m = len(a)
else:
    k = c
    m = len(a)/c
for i in range(0, k):
    j = i
    temp1 = a[i]
    for l in range(0, m):
        temp2 = a[(j+c) % len(a)]
        a[(j+c) % len(a)] = temp1
        j = (j+c) % len(a)
        temp1 = temp2
        print(a, temp1)
print(a)
