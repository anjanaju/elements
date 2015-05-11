__author__ = 'anjana'
class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None

    def rangequery(self, l, u, lt):
        if self.item <= l:
            if self.item == l:
                lt.append(self.item)
            if self.right is not None:
                self.right.rangequery(l,u, lt)
        elif self.item >= u:
            if self.item == u:
                lt.append(self.item)
            if self.left is not None:
                self.left.rangequery(l, u, lt)
        elif self.item > l and self.item < u:
            lt.append(self.item)
            if self.left is not None:
                self.left.rangequery(l, self.item, lt)
            if self.right is not None:
                self.right.rangequery(self.item, u, lt)
        else:
            return


class Tree:
    def __init__(self, x):
        self.root = x

    def findrange(self, l, u):
        lt = list()
        self.root.rangequery(l, u, lt)
        print(lt)

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
t.findrange(3, 10)