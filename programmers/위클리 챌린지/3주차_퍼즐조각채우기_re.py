# dfs 이용해 game_board의 빈자리 또는 table의 블럭 인덱스 리스트 저장
def dfs(i,j,board, visited, empty, n):
    section = []
    stack = [(i,j)]
    while stack:
        x,y = stack.pop()
        if x >= 0 and x < len(board) and y >= 0 and y < len(board):   # 음수인 인덱스 걸러내기
            if visited[x][y] == False and board[x][y] == n:
                visited[x][y] = True
                section.append((x,y))

                stack.append((x-1, y))
                stack.append((x+1, y))
                stack.append((x, y-1))
                stack.append((x, y+1))
    empty.append(sorted(section))

# 순차적으로 모든 칸 탐색하기 위해 game_board의 빈공간의 위치를 (0,0)을 기준으로 변경
 # 이 때 좌표를 나타내는 튜플값은 변경이 불가하므로 다시 만들어서 return 해준다.
def standard(b):
    tmp = []
    std_x = b[0][0]
    std_y = b[0][1]
    for x,y in b:
        tmp.append((x-std_x, y-std_y))
    return sorted(tmp)


def solution(game_board, table):
    ans = []
    N = len(game_board)

    visited_board = [[False for _ in range(N)] for _ in range(N)]
    blank_list = []      # game_board의 빈자리 좌표 리스트

    visited_table = [[False for _ in range(N)] for _ in range(N)]
    block_list = []      # table의 블록 좌표 리스트

    # dfs 이용하여 game_board의 빈 자리 좌표 리스트 blank에 저장
    for i in range(N):
        for j in range(N):
            if visited_board[i][j] == False and game_board[i][j] == 0:
                dfs(i,j, game_board, visited_board, blank_list,0)

    # dfs 이용하여 table의 블럭 좌표 리스트 block에 저장
    for i in range(N):
        for j in range(N):
            if visited_table[i][j] == False and table[i][j] == 1:
                dfs(i,j,table,visited_table,block_list,1)

    # standard 함수 이용해서 blank의 블록 좌표를 (0,0) 기준으로 변경 후 blocks에 저장
    blocks = []
    print(block_list)
    for block in block_list:
        blocks.append(standard(block))

    # 2차원 리스트 한칸씩 돌면서 맞는 자리 있는지 확인
    def match(block):
        for x in range(N):
            for y in range(N):
                move = []
                for dx, dy in block:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and ny >= 0 :    # 인덱스 체크
                        try:
                            move.append((x+dx, y+dy))
                        except IndexError:
                            break
                    else:
                        break
                if len(block) == len(move) and move in blank_list:  # 맞는 자리 찾기
                    blank_list.remove(move)     # 자리 찾았으면 인덱스 삭제
                    ans.extend(move)
                    return True
        return False

    # 블럭 90도 회전
    def rotate_90(block):
        new = []
        for x,y in block:
            new.append((y, N-1-x))
        return standard(new)

    # 블럭 하나씩 맞는 자리 있는지 살펴보고 없으면 회전 후 찾기 반복
    for block in blocks:
        for _ in range(4):
            if match(block) == False:
                block = rotate_90(block)
            else:
                break
    return len(ans)


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))

print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))
