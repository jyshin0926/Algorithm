## Traveling Salesman Problem

# 외판원 순회는 NP문제로 N이 16개 이하일 때 DP와 비트마스크를 이용
# DP는 특정 도시들을 방문한 상태일 때 최소 비용을 저장해 놓고 이를 사용
# 비트마스크는 특정 도시를 방문한 상태를 저장할 때 사용
# memoization(대표적으로 피보나치 수열은 Top-Down 방식으로 구할 때 사용)을 이용하여 이미 구한최소 비용을 다시 구하는 시간 낭비를 방지
# 최소 비용 저장 위해 2차원 배열 사용. 행과 열은 최소 비용이 같을 조건 즉, 이미 방문한 도시들의 집합과 현재 있는 도시 번호
# d[i][j] = 이미 방문한 도시들의 집합이 i이고 현재 있는 도시가 j 일 때, 방문하지 않은 나머지 도시들을 모두 방문한 뒤 출발 도시로 돌아올 때 드는 최소 비용

N = int(input())
W = [list(map(int, input().split())) for i in range(N)]   # 도시 행렬
INF = 987654321 # 정점 중 최단 경로를 갱신 # 시작점을 제외한 아직 방문하지 않은 정점은 가장 큰 수(INF) 로 초기화
DP = [[-1 for _ in range(1 << N)] for _ in range(N)]     # 1 << n : n번째 비트 켜기


def TSP(curr, visited):
    if DP[curr][visited] != -1:
        return DP[curr][visited]
    if visited == (1 << N) - 1:   # n개의 비트를 모두 켠다 # n개의 도시를 모두 방문
        if W[curr][0]:
            return W[curr][0]
        return INF
    ret = INF
    for i in range(N):
        if visited & (1 << i) == 0 and W[curr][i] != 0:
            ret = min(ret, W[curr][i] + TSP(i, visited | (1 << i)))     # 최소값 갱신
    DP[curr][visited] = ret
    return ret

