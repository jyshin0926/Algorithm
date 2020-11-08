def solution(m,n,puddles):
    routes = [[0]*(m+1) for _ in range(n+1)]
    routes[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i,j) == (1,1):
                continue
            elif [j,i] in puddles:
                continue
            routes[i][j] += (routes[i-1][j] + routes[i][j-1])
    return routes[-1][-1] % 1000000007

# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수
# 물 웅덩이 피해서 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return
# 점화식 필요