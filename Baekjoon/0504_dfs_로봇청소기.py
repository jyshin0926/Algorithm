n,m = map(int, input().split())
r,c,d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 1
x, y = r, c
grid[x][y] = 2 # 방문처리

while True:
    visited = False
    for i in range(4):
        d = (d-1) % 4
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0:
                cnt += 1
                grid[nx][ny] = 2
                x,y = nx, ny
                visited = True
                break
    if not visited:
        nx = x - directions[d][0]
        ny = y - directions[d][1]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 2:
                x, y = nx, ny
            elif grid[nx][ny] == 1:
                print(cnt)
                break
        else:
            print(cnt)
            break


