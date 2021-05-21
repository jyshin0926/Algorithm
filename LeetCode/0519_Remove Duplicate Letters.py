from collections import Counter
class Solution:
# Runtime: 48 ms, faster than 17.33% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 14.4 MB, less than 51.46% of Python3 online submissions for Remove Duplicate Letters.
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s); stack = []
        for x in s:
            counter[x] -= 1
            if x in stack:
                continue
            while stack and x < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(x)
        return ''.join(stack)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for x in sorted(set(s)):
            suf = s[s.index(x):]
            if set(s) == set(suf):
                return x + self.removeDuplicateLetters(suf.replace(x, ''))
        return ''

        # s 돌면서 이후에 같은 Letter 있으면 pop(0)
        # 체크하다가 안 나온 알파벳 다음에 그 앞에 나온 것들도 있는지 체크

# Wrong Answer(input:'ecbacba')
#     def removeDuplicateLetters(self, s: str) -> str:
#         tmp = []; s = list(s)
#         while len(s) > 0:
#             for i in range(len(s)):
#                 if s[i] not in tmp:  # 최초 문자는 붙이기
#                     tmp.append(s.pop(i))
#                 elif s[i] in tmp:
#                     if tmp[-1] > s[i]:
#                         if s[i] == tmp[0]:
#                             tmp.remove(s[i])
#                             tmp.append(s.pop(i))
#                         s.pop(i)
#                     else:
#                         tmp.remove(s[i])
#                         tmp.append(s.pop(i))
#                 break
#         return ''.join(tmp)

print(Solution().removeDuplicateLetters('bcabc'))
print(Solution().removeDuplicateLetters('cbacdcbc'))  # acdb
print(Solution().removeDuplicateLetters('bcabc'))  # acdb
print(Solution().removeDuplicateLetters("ecbacba"))  # eacb


# 첫번째

# n = 1; sum = 0
# while n != 0:
#     n = int(input())
#     if n > 0:
#         sum += n
#     elif n < 0:
#         continue
# print(sum)

# 첫번째 나온 알파벳들만 순서대로 저장


