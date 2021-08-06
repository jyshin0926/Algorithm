# 투포인터가 중앙을 중심으로 확장하는 형태로 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            print('left:',left, 'right:',right)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print('s[left+1:right]:',s[left+1:right])
            return s[left+1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(0,len(s)):
            result = max(result,
                         expand(i, i+1),  # 짝수용 투포인터
                         expand(i, i+2),  # 홀수용 투포인터
                         key=len)
        return result

print(Solution().longestPalindrome(s = "babad"))
print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('a'))
print(Solution().longestPalindrome('ac'))







