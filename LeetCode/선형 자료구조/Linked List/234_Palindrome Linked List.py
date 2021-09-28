from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 데크자료형 선언
        q = []
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            return True

print(Solution().isPalindrome([1,2,2,1]))
print(Solution().isPalindrome([1,2]))