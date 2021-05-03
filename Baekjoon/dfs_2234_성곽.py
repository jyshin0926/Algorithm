n, m = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(m)]
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
cnt, max_size, new_max = 0, 0, 0
visited = [[0]*n for _ in range(m)]
area = [0]*(n*m+1)

def dfs(x, y, z):
    visited[x][y] = z
    res = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not ((wall[x][y] & (1<<i)) or visited[nx][ny]):
            res += dfs(nx, ny, z)
    return res

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            k = dfs(i, j, cnt)
            max_size = max(max_size, k)
            area[cnt] = k
for i in range(m):
    for j in range(n):
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                continue
            x, y = visited[i][j], visited[ni][nj]
            if x != y:
                new_max = max(new_max, area[x]+area[y])
print("%d\n%d\n%d" % (cnt, max_size, new_max))
