## BFS
# bfs는 재귀 안 쓰므로 sytresursionlimit 안해줘도 됨
from collections import deque

# 세로, 가로, 개수 입력받고 초기 설정
n,m,k = map(int,input().split())
array = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))
    cnt = 1
    visited[i][j] = True
    while q:
        x, y = q.popleft()      # popleft() : pop()의 반대로, 왼쪽(앞쪽)에서 부터 차례대로 제거와 반환(remove and return)을 하는 메소드
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:   # nx, ny가 2차원 배열에 포함되어 있으면
                continue
            if array[nx][ny] and not visited[nx][ny]:    # 쓰레기 떨어진 곳(값이 1인 곳)만 방문 # 해당 원소를 방문하지 않은 경우 방문하도록 처리
                q.append((nx, ny))      # 새로운 노드 탐색
                visited[nx][ny] = True
                cnt += 1
    return cnt

for _ in range(k):   # 쓰레기 떨어진 좌표 입력받기
    r, c = map(int, input().split())
    array[r - 1][c - 1] = 1
for i in range(n):      # 세로
    for j in range(m):  # 가로
        if not visited[i][j] and array[i][j]:   # 그 정점이 방문되지 않았을 경우에만 반복
            ans = max(ans, bfs(i,j))    # 모든 정점에 대해 bfs 반복 수행하며 갱신
print(ans)
