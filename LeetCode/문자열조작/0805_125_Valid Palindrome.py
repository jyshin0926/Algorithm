# 내 코드
# Runtime: 32 ms, faster than 98.54% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.2 MB, less than 35.52% of Python3 online submissions for Valid Palindrome.

import re
def isPalindrome(s):
    s = ''.join(re.findall('[A-Za-z0-9]+',s)).lower()
    if s == s[::-1]:   # s == ''.join(reversed(s)) 로 해도 동일하나 슬라이싱이 처리속도가 훨씬 빠름
        return True
    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama"))


# 참고 코드3: 슬라이싱 사용
# 정규식으로 필터링하고 슬라이싱
# isalnum()은 모든 문자를 일일이 점검하나, 정규식은 문자열 전체를 한 번에 영숫자만 걸러냄
# 오 내 코드보다 더 간결하다..
# Runtime: 36 ms, faster than 95.48% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.7 MB, less than 23.68% of Python3 online submissions for Valid Palindrome.
def sol3(s):
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]  # 슬라이싱


# 참고 코드2: 데크 자료형을 이용한 최적화
# 데크를 명시적으로 선언하면 리스트보다 좀 더 속도 높일 수 있음
# Runtime: 44 ms, faster than 77.31% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19.1 MB, less than 16.49% of Python3 online submissions for Valid Palindrome.
from collections import deque
def sol2(s):
    # 자료형 데크로 선언
    strs = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 참고 코드1: 리스트로 변환
# Runtime: 284 ms, faster than 5.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 20 MB, less than 5.91% of Python3 online submissions for Valid Palindrome.
def sol1(s):
    strs = []
    for char in s:
        if char.isalnum():  # isalnum : 영문자, 숫자 여부 판별
            strs.append(char.lower())
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True