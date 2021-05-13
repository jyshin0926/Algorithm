class Solution:
    # dp
    # Runtime: 104 ms, faster than 97.96% of Python3 online submissions for Longest Palindromic Substring.
    # Memory Usage: 14.2 MB, less than 81.90% of Python3 online submissions for Longest Palindromic Substring.
    def longestPalindrome_dp(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start,length = 0,0
        for i in range(len(s)):
            if s[i-length:i+1] == s[i-length:i+1][::-1]:
                start,length = i-length, length+1
                print(i-length)
            elif i-length > 0 and s[i-length-1:i+1] == s[i-length-1:i+1][::-1]:
                start,length = i-length-1, length+2
        return s[start:start+length]

        # 귀류법(모순 증명법)
        # https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
        # Runtime: 96 ms, faster than 98.48% of Python3 online submissions for Longest Palindromic Substring.
        # Memory Usage: 14.4 MB, less than 37.56% of Python3 online submissions for Longest Palindromic Substring.
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ''
        max_len = 1  # 가장 긴 팰린드롬 길이 저장하고 갱신할 변수
        start = 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2  # 이게 팰린드롬인지
                continue
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1  # 이게 팰린드롬인지 체크
        return s[start:start + max_len]

if __name__ == '__main__':
    for x in ['babad','cbbd','a','ac']:
        print(Solution().longestPalindrome(x))
        print(Solution().longestPalindrome_dp(x))




