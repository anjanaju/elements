__author__ = 'anjana'
def generate(d, a, i, n, b, l):
    if i==n:
        l.append(list(b))
        return
    j = int(a[i])
    k = d[j]
    for e in k:
        b[i] = e
        generate(d, a, i+1, n, b, l)

d = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l']}
print(d)
a = '3254'
n = 4
b = ['a', 'a', 'a', 'a']
l = list()
generate(d,a,0,n,b,l)
for e in l:
    print(e)