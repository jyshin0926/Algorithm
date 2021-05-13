# n개 물건
# 무게 w, 가치 v
# 최대 k 무게 넣을 수 있는 배낭
# 물건들의 가치 최댓값 출력

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1,n+1):
    weight, val = map(int, input().split())
    for j in range(1,k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+val)
print(dp[n][k])