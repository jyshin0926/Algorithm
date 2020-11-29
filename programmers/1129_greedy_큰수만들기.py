# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
# k는 1 이상 number의 자릿수 미만인 자연수

def solution(number, k):
    tmp = []
    number = list(number)
    for x in number:
        while tmp and tmp[-1] < x and k > 0:
            tmp.pop()
            k -= 1
        tmp.append(x)
    if k > 0:
        tmp = tmp[:-k]

    ans = ''.join(tmp)
    return ans

print(solution('10000', 2))
print(solution('1231234', 3))
print(solution('4177252841', 7))

# 테스트 8 〉	통과 (17.30ms, 11.5MB)
# 테스트 9 〉	통과 (35.18ms, 16MB)
# 테스트 10 〉	통과 (87.80ms, 17MB)