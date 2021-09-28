from typing ListNode
class MyCircularDeque:
    def __init__(self,k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0  # 최대길이정보, 현재길이정보
        self.head.right, self.tail.left = self.tail, self.head

    def insertFront(self,val):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self,value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def _add(self,node):