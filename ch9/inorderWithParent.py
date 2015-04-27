__author__ = 'anjana'


class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self, x):
        self.root = x

    def inorderNode(self):
        if self.root is None:
            return
        curr = self.root
        prev = None
        next = None
        while curr is not None:
            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left is not None:
                    next = curr.left
                else:
                    print(curr.item)
                    if curr.right is not None:
                        next = curr.right
                    else:
                        next = curr.parent
            elif curr.left == prev:
                print(curr.item)
                if curr.right is not None:
                    next = curr.right
                else:
                    next = curr.parent
            else:
                next = curr.parent
            prev = curr
            curr = next

t1 = Treenode(1)
t2 = Treenode(2)
t3 = Treenode(3)
t4 = Treenode(4)
t5 = Treenode(5)

t4.right = t5
t5.parent = t4
t4.left = t2
t2.parent = t4
t2.left = t1
t1.parent = t2
t2.right = t3
t3.parent = t2

t = Tree(t4)
t.inorderNode()
print("done")