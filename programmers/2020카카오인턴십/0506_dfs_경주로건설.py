def solution(board):
    length = len(board)
    def dfs(i,j):
        directions = [(1,0),(0,1)]
        if i < 0 or i >= length or j < 0 or j>=length or board[i][j] != 0:
            return
        board[i][j] = 1
        for dx,dy in directions:
            nx = i+dx
            ny = j+dy
            dfs(nx,ny)

    cnt = 0
    for i in range(length):
        for j in range(length):
            if board[i][j] == 0:
                dfs(i,j)
                cnt += 1

    return cnt

if __name__ == '__main__':
    for x in [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
              [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
              [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]:
        print(solution(x))