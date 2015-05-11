__author__ = 'anjana'
class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, x):
        self.root = x
    def lca(self, i, j):
        if i<j:
            temp = i
            i=j
            j = temp
        t = self.root
        while t is not None:
            if (i>=t.item  and j<=t.item) or i==t.item or j==t.item:
                return t.item
            elif i<t.item:
                t = t.left
            else:
                t = t.right
        return None




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
print(t.lca(2, 11))