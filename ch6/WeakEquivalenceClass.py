__author__ = 'anjana'


def FindEqu(a, b, n):
    l = list()
    for i in range(0, n):
        l.append(-1)
    for i in range(len(a)):
        if (l[a[i]] == -1) and (l[b[i]] == -1):
            if (a[i] > b[i]):
                k = b[i]
            else:
                k = a[i]
            l[a[i]] = k
            l[b[i]] = k
        elif (l[b[i]] == -1):
            l[b[i]] = l[a[i]]
        else:
            l[a[i]] = l[b[i]]
    d = dict()
    for i in range(0, n):
        if (l[i] == -1):
            d[i] = [i]
        else:
            if d.__contains__(l[i]):
                d[l[i]].append(i)
            else:
                d[l[i]] = [i]
    for i in d.values():
        print(i)


a = [0, 1, 2, 5]
b = [3, 5, 1, 6]

FindEqu(a, b, 7)