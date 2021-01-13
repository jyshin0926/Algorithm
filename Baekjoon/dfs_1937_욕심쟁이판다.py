import sys
sys.setrecursionlimit(100000)
def dfs(x, y):
    if visited[x][y] == -1:  # if문을 걸어줘야 시간초과 안 남!
        visited[x][y] = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and array[x][y] < array[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny))
        visited[x][y] += 1
    return visited[x][y]

n = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # dfs 함수 밖으로 빼줘야 시간이 덜 걸린다.(dfs함수 안에 넣으면 900ms, 밖으로 빼면 892ms)
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)

