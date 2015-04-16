class ListNode:
    def __init__(self, item, ptr=None):
        """

        :rtype : ListNode
        """
        self.item = item
        self.ptr = ptr


class MyList:
    def __init__(self, head):
        self.head = head

    def reverse(self):
        if self.head is None or self.head.ptr is None:
                return self
        cur1 = self.head
        cur2 = self.head.ptr
        cur1.ptr = None
        while cur2 is not None:
            temp = cur2.ptr
            cur2.ptr = cur1
            cur1 = cur2
            cur2 = temp
        self.head = cur1


    def printlist(self):
        ln = self.head
        while ln is not None:
            print(ln.item )
            ln = ln.ptr


ln3 = ListNode(3)
ln2 = ListNode(2, ln3)
ln1 = ListNode(1, ln2)

l = MyList(ln1)
l.printlist()
l.reverse()
l.printlist()


