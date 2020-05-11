num = int(input())
dp = [[0]*10 for i in range(num+1)]     # # dp[num][10] 이렇게 선언해주면 0~9의 마지막 숫자 저장 가능
for i in range(10):
    dp[0][i] = 1            # dp[0][0~9]를 모두 1로 초기화
for i in range(num+1):      # i는 0~num     # 자리 수(num)
    for j in range(10):     # j는 0 ~ 9     # j는 맨 끝에 오는 숫자 예) dp[1][2]는 _2로 끝나는 것을 체크. 2보다 작거나 같은 숫자가 오면 됨
        for k in range(j+1):    # k는 j ~ 9
            dp[i][j] += dp[i-1][k]   # 점화식   # i-1 내에서 j 까지의 모든 경우의 수를 더하기

print(dp[num][9] % 10007)

# print(dp)
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]]
