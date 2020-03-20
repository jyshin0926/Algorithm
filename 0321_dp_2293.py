n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coin:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]    # 각각의 동전(i= 1,2,5)을 더해 숫자 나타내기
print(dp[k])
