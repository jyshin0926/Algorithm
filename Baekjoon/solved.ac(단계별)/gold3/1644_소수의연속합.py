# two pointer
import sys
n = int(sys.stdin.readline())
ans = 0

# 에라토스테네스의 체
def isPrime(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:            # i가 소수인 경우
            for j in range(2*i, n+1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2,n+1) if sieve[i] == True]


# 투포인터로 연속합 구하기
tmp = isPrime(n)
left, right = 0, 0
while right <= len(tmp):
    val = sum(tmp[left:right])
    if val == n:
        ans += 1
        left += 1
    elif val < n:
        right += 1
    else:
        left += 1
print(ans)



# 연속된 소수의 합으로 나타낼 수 있는 경우의 수
# n에서 소수를 하나씩 빼봐서
