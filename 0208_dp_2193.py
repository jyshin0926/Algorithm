## 피보나치 수열 개념과 동일 ##
import sys
N = int(sys.stdin.readline())
dp = [0, 1, 1]
for i in range(3, N+1):
    dp.append(dp[i-1] + dp[i-2])
print(N)
#print(dp)  # N=5 일 때   # [0, 1, 1, 2, 3, 5]