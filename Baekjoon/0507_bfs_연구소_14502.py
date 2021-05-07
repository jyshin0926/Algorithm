from collections import deque
from itertools import combinations
import copy

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(n)]

room = []; virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            room.append([i,j])
        elif lab[i][j] == 2:
            virus.append([i,j])

candidate_walls = list(combinations(room,3))
directions = [(-1,0),(0,1),(1,0),(0,-1)]
res = 0

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    visited[r][c]=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2
                visited[nx][ny] = 1
                queue.append([nx,ny])


for walls in candidate_walls:
    new_lab = copy.deepcopy(lab)
    w1, w2, w3 = walls
    visited = [[0]*m for i in range(n)]
    cnt = 0

    new_lab[w1[0]][w1[1]]=1
    new_lab[w2[0]][w2[1]]=1
    new_lab[w3[0]][w3[1]]=1

    for j in virus:
        j1, j2 = j
        bfs(j1, j2)

    for k in new_lab:
        cnt += k.count(0)

    res = max(res, cnt)
print(res)














#