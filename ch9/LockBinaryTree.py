__author__ = 'anjana'


class Treenode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        self.islock = False
        self.numChildrenLocked = 0

    def islock(self):
        return self.islock


    def lock(self):
        if self.islock or (self.numChildrenLocked > 0):
            return False;
        temp = self.parent
        while temp is not None:
            if temp.islock:
                return False
            temp = temp.parent

        temp = self.parent
        while temp is not None:
            temp.numChildrenLocked += 1
            temp = temp.parent

        self.islock = True
        return True

    def unlock(self):
        temp = self.parent
        while temp is not None:
            temp.numChildrenLocked -= 1
            temp = temp.parent
        self.islock = False


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

print(t1.lock())
print(t2.lock())
t1.unlock()
print(t4.lock())
print(t1.lock())
print("done")