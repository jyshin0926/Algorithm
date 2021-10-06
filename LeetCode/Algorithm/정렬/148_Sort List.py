# 병합정렬 이용
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        result = self.mergeTwoLists(l1,l2)
        return result


# ListNode(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
# print(sortList(ListNode()))

# a = ListNode(-1)
# b = ListNode(5)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(0)

a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)

a.next = b
b.next = c
c.next = d
#d.next = e
Sol = Solution()
Sol.sortList(a)


# 원래 넣은 값 중 가장 작은 수를 갖는 값부터 출력해야 함
while True:
    try:
        print(c.val)
        c = c.next
    except Exception as E:
        break