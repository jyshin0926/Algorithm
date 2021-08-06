from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

    # 또 다른 pythonic한 코드
    def sol2(self, s: List[str]) -> None:
        s.reverse()

    # 투포인터 사용한 스왑
    # 속도는 위에 코드들보다 느림
    def sol3(self, s:List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1