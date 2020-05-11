n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k+1)]
for i in range(1, k+1):
    arr = []
    for j in coin:
        if i-j >= 0 and dp[i-j] != -1:
            arr.append(dp[i-j])
    if not arr:
        dp[i] = -1
    else:
        dp[i] = min(arr) + 1    # dp[i] = min(dp[i-coin]) + 1
print(dp[k])
