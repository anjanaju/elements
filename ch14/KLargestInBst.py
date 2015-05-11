class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None

    def klargestnode(self, k, l):
        rsize = 0

        if self.right is not None:
            rsize = self.right.klargestnode(k, l)
            if rsize == k:
                return rsize
            else:
                l.append(self)
                if self.left is not None:
                    lsize = k-rsize-1
                    if lsize > 0:
                        lsize = self.left.klargestnode(lsize, l)
                        return lsize+rsize+1
                    else:
                        return k
                else:
                    return rsize+1
        else:
            l.append(self)
            if self.left is not None:
                return 1+self.left.klargestnode(k-1, l)
            else:
                return 1

class Tree:
    def __init__(self, x):
        self.root = x

    def klargest(self, k):
        l = list()
        self.root.klargestnode(k, l)
        for e in l:
            print(e.item)

t1 = Treenode(7)
t2 = Treenode(3)
t3 = Treenode(2)
t4 = Treenode(5)
t5 = Treenode(11)
t6 = Treenode(10)
t7 = Treenode(13)

t1.left = t2
t1.right = t5
t2.left = t3
t2.right = t4
t5.left = t6
t5.right = t7
t = Tree(t1)
t.klargest(5)