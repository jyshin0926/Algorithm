# 에라토스테네스의 체
from itertools import permutations

def check(num_list):
    ans = 0
    for n in num_list:
        cnt = 0
        for i in range(2,n):
            if n % i == 0:
                cnt += 1
                break
        if n > 1 and cnt == 0:
            ans += 1
    return ans

def solution(numbers):
    num_list = []
    for i in range(1, len(numbers)+1):
        tmp = permutations(numbers,i)
        for x in tmp:
            num_list.append(int(''.join(x)))
    num_list = list(set(num_list))
    return check(num_list)

# 테스트 1 〉	통과 (0.24ms, 10.2MB)
# 테스트 2 〉	통과 (153.45ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (2122.81ms, 10.5MB)

print(solution('17'))
print(solution('011'))