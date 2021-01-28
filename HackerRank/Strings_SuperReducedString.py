# Complete the superReducedString function below.
# while문 때문에 시간초과
# def superReducedString(s):
#     tmp = [x for x in s]
#     while True:
#         if len(tmp) == len(set(tmp)):
#             break
#         for a, b in zip(tmp, tmp[1:]):
#             if a == b:
#                 tmp.remove(a)
#                 tmp.remove(b)
#             else:
#                 continue
#     if len(tmp) == 0:
#         return 'Empty String'
#     else:
#         return ''.join(tmp)

# while문 없애고 tmp 빈 배열 선언 후 차례로 체크하도록 변경
def superReducedString(s):
    tmp = []
    for val in s:
        if tmp and val == tmp[-1]: # 빈 배열이니까 tmp 조건 같이 써주기
            tmp.pop()
        else:
            tmp.append(val)
    if len(tmp) == 0:
        return 'Empty String'
    else:
        return ''.join(tmp)


print(superReducedString('aaabccddd'))
print(superReducedString('aa'))
print(superReducedString('baab'))
print(superReducedString('zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'))
