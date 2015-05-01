__author__ = 'anjana'
a = [3, 1 , 0, 2]

for i in range(len(a)):
    if a[i]<= 0:
        continue
    j = a[i]
    k = i
    start = True
    while k!= i or start:
         temp = a[j]
         a[j] = -k
         k = j
         j = temp
         print(j,k)
         start = False
    print(a)

for i in range(len(a)):
        a[i] = -a[i]
print(a)