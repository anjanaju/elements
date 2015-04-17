__author__ = 'anjana'
def findpairs(l):
    d = dict()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in d:
                d[l[i][j]].append(i)
            else:
                d[l[i][j]] = [i]
    for i in d.keys():
        print(i, d[i])

    count = dict()
    for i in d.keys():
        j = d[i]
        for m in range(len(j)):
            n= m+1
            while n<len(j):
                if (j[m], j[n]) in count:
                    count[(j[m], j[n])] = count[(j[m], j[n])] +1
                else:
                    count[(j[m], j[n])] = 1
                n = n+1

    for i in count.keys():
        print(i, count[i])


l = [['ab', 'bc', 'cd'], ['ab', 'cd', 'be'], ['bc', 'ce']]
findpairs(l)