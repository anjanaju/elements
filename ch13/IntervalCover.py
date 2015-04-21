__author__ = 'anjana'
class Endpoint:
    def __init__(self, x, isleft, id):
        self.x = x
        self.isleft = isleft
        self.id = id


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
        return '({}, {}, {})'.format(self.x, self.isleft, self.id)


l = [(1, 5), (6, 10), (11, 13), (4, 5)]
es = list()
for i in range(len(l)):
    es.append(Endpoint(l[i][0], 1, i))
    es.append(Endpoint(l[i][1], 0, i))

print(es)
es = sorted(es)
print(es)

d = dict()
for e in es:
    if e.isleft == 1:
        d[e.id] = 1
    else:
        if d.keys().__contains__(e.id):
            print(e.x)
            d.clear()
