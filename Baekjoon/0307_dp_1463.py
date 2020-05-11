# 재귀함수를 매번 호출하면 시간복잡도가 굉장히 커지므로 다이나믹 프로그래밍 즉, 리스트를 만들어 값을 매번 저장해주는 것이 속도 향상에 도움이 된다.
# 입력받고 초기 설정
x = int(input())
dp = []
dp.append(0)    # 0
dp.append(0)    # 1
dp.append(1)    # 2
dp.append(1)    # 3

# 점화식
for i in range(4, x+1):
    dp.append(dp[i-1]+1)    # dp[i] 에 저장
    if i % 2 == 0:  # 2로 나눠질 때
        dp[i] = min(dp[i],dp[i//2]+1)   # 비교하여 최소값 채택
    if i % 3 == 0:  # 3으로 나눠질 때
        dp[i] = min(dp[i],dp[i//3]+1)   # 비교하여 최소값 채택
print(dp[x])
