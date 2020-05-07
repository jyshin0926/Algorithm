T = int(input())
for _ in range(T):
    n = int(input())
    dp = [1, 2, 4]      # 1~3의 경우 초기 설정
    for i in range(3, n):
        dp.append(sum(dp[-3:]))     # 점화식
    print(dp[-1])
