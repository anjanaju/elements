__author__ = 'anjana'


class Endpoint:
    def __init__(self, x, isleft, c, h):
        self.x = x
        self.isleft = isleft
        self.c = c
        self.h = h

    def __cmp__(self, other):
        if self.x < other.x:
            return -1
        elif self.x == other.x:
            if self.isleft == False and other.isleft == True:
                return -1
            elif self.isleft == True and other.isleft == False:
                return 1
            else:
                return 0
        else:
            return 1

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.x, self.isleft, self.c, self.h)


l = [(1, 5, 1, 1), (6, 10, 2, 1), (11, 13, 3, 1), (4, 5, 4, 3)]
es = list()
for p in l:
    es.append(Endpoint(p[0], 1, p[2], p[3]))
    es.append(Endpoint(p[1], 0, p[2], p[3]))

print(es)
es = sorted(es)
print(es)

d = dict()

# it prints (x, c) where color starts from x
for e in es:
    if e.isleft == 1:
        d[e.h] = e
        maxe = d[max(d.keys())]
        print(maxe.x, maxe.c)
    else:
        d.__delitem__(e.h)
        if d.__len__() > 0:
            maxe = d[max(d.keys())]
            print(maxe.x, maxe.c)
        else:
            print(e.x, 'blank')

