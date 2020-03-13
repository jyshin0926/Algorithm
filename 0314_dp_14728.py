# knapsack 문제 알고리즘으로 해결
# bottom-up

# 단원의 수가 N, 총 공부시간이 T
# dp 를 이용하여 시간 복잡도 O(NT)로 문제 해결 가능

n, t = map(int, input().split())            # n : 단원 개수, t: 공부할 수 있는 총 시간
dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1, n+1):
    k, s = map(int, input().split())        # k: 단원별 예상 공부 시간 , s: 단원 문제의 배점
    for j in range(1, t+1):
        if j < k:                           # 총 시간 < 단원 공부 시간
            dp[i][j] = dp[i-1][j]
        else:                               # 총 시간 >= 단원 공부 시간
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)    # 그 행의 이전까지의 최대점수 vs (이전까지 구했던 결과 중 최대 점수+현재 단원의 배점)
print(dp[n][t])






## 다른 풀이
import sys
sys.setrecursionlimit(100000)

def cram(L, time, score, n):    # L:가능한 총 공부시간, time: 각 단원 공부시간, score: 각 단원의 배점, n: 단원 개수
    profit = [[0 for _ in range(L+1)] for _ in range(n+1)]     # dp를 위한 2차원 리스트 초기화
    for i in range(n+1):    # 행
        for t in range(L+1):    # 열
            if i==0 or t==0:    # 0번째 행과 열은 0으로 세팅
                profit[i][t] = 0
            elif time[i-1] <= t:    # 점화식
                profit[i][t] = max(score[i-1] + profit[i-1][t-time[i-1]], profit[i-1][t])   # 최대값 선택하여 갱신
            else:
                profit[i][t] = profit[i-1][t]
    return profit[n][L]


time = []
score = []
N, T = map(int, sys.stdin.readline().split())
for _ in range(N):
    K, S = map(int, sys.stdin.readline().split())
    time.append(K)
    score.append(S)
print(cram(T, time, score, N))

