from collections import deque

def bfs(visited, n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]

        for nx in (x+1, x-1, 2*x):
            if 0 <= nx <= 10**6 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

n, k = map(int, input().split())
visited = [0] * (10**6)
print(bfs(visited, n, k))