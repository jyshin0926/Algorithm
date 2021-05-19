# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         tmp = []; s = list(s)
#         while len(s) > 0:
#             for i in range(len(s)):
#                 if s[i] not in tmp:  # 최초 문자는 붙이기
#                     tmp.append(s.pop(i))
#                 elif s[i] in tmp:
#                     if tmp[-1] > s[i]:
#                         #if s[i] == tmp[0]:
#                         for x in tmp:
#                             if x < s[i] and tmp.index(x) < tmp.index(s[i]):
#                                 tmp.remove(s[i])
#                                 tmp.append(s.pop(i))
#                         s.pop(i)
#                     else:
#                         tmp.remove(s[i])
#                         tmp.append(s.pop(i))
#                 break
#         return ''.join(tmp)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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

        for x in sorted(set(s)):
            #print('sorted(set(s)):',sorted(set(s)))
            #print(x)
            suf = s[s.index(x):]
            #print('suf:',set(suf))
            #print('set(s):',set(s))

            if set(s) == set(suf):
                #print('update ans:', x + self.removeDuplicateLetters(suf.replace(x, '')),'\n')
                return x + self.removeDuplicateLetters(suf.replace(x, ''))
        return ''

        # s 돌면서 이후에 같은 Letter 있으면 pop(0)
        # 체크하다가 안 나온 알파벳 다음에 그 앞에 나온 것들도 있는지 체크


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


