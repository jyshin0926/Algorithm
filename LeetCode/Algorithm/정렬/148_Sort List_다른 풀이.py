# 내장 함수 이용

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

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


# 원래 값 크기 상관없이 가장 먼저 넣은 값(a)을 먼저 넣어서 출력해야 함
while True:
    try:
        print(a.val)
        a = a.next
    except Exception as E:
        break
