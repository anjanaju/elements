__author__ = 'anjana'


class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None

    def convert(self):
        lstart = None
        lend = None
        rstart = None
        rend = None
        if self.left is not None:
            (lstart, lend) = self.left.convert()
            lend.right = self
            self.left = lend
        else:
            lstart = self
        if self.right is not None:
            (rstart, rend) = self.right.convert()
            rstart.left = self
            self.right = rstart
        else:
            rend = self
        return (lstart, rend)


class Tree:
    def __init__(self, x):
        self.root = x


    def converttodll(self):
        (start, end) = self.root.convert()
        self.root = start

    def printlist(self):
        t = self.root
        while t is not None:
            print(t.item)
            t = t.right


t1 = Treenode(7)
t2 = Treenode(3)
t3 = Treenode(2)
t4 = Treenode(5)
t5 = Treenode(11)
t1.left = t2
t1.right = t5
t2.left = t3
t2.right = t4
t = Tree(t1)
t.converttodll()
t.printlist()