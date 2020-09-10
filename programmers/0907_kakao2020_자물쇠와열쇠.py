import math

# 참고 : https://jay-ji.tistory.com/41
# https://johnyejin.tistory.com/127
# 시계 방향으로 90도 회전
def rotation(arr):
    rt_arr = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            rt_arr[i][j] = arr[j][i]
        rt_arr[i] = rt_arr[i][::-1]
    return rt_arr

def is_unlock(bg_size, _lock, _key, start_x, start_y, c_start, c_end):
    bg = [[0] * bg_size for _ in range(bg_size)]

    # 확장된 배열인 background bg에 key 놓기
    for i in range(len(_key)):
        for j in range(len(_key)):
            bg[start_y+i][start_x+j] += _key[i][j]

    # 확장된 배열인 background bg에 lock 놓기
    for i in range(c_start, c_end):
        for j in range(c_start, c_end):
            bg[i][j] += _lock[i - c_start][j - c_start]
            # lock + key == 1이 아닌 경우 False
            if bg[i][j] != 1:
                return False
    return True



def move(arr,lock_arr,direction):
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우 이동
    up = directions[0]
    down = directions[1]
    left = directions[2]
    right = directions[3]
    move_arr = [['throw' for _ in range(len(arr)+len(lock_arr))] for _ in range(len(arr)+len(lock_arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if direction == 'up':
                nx, ny = i + up[0], j + up[1]
                move_arr[nx][ny] = arr[i][j]
            elif direction == 'down':
                nx, ny = i + down[0], j + down[1]
                move_arr[nx][ny] = arr[i][j]

            elif direction == 'left':
                nx, ny = i + left[0], j + left[1]
                move_arr[nx][ny] = arr[i][j]

            elif direction == 'right':
                nx, ny = i + right[0], j + right[1]
                move_arr[nx][ny] = arr[i][j]
    return move_arr


def solution(_key, _lock):
    lock_size = len(_lock)
    c_start = len(_key) - 1 # center 좌표(expandList에서 lock의 시작 지점)
    c_end = c_start + lock_size # expandList에서 lock이 끝나는 지점
    bg_size = lock_size + (2 * c_start) # expandList 배열의 크기(처음부터 1개 겹쳐서 비교하기 위해)

    # lock은 고정이고 key가 움직이도록
    for x in range(0,4):
        for i in range(0, c_end):
            for j in range(0,c_end):
                if is_unlock(bg_size, _lock, _key, i,j,c_start,c_end) is True:
                    return True
        # key를 90도 돌린다.
        _key = rotation(_key)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# key 회전 먼저
# key 이동하여 lock에 맞추기
# 열쇠는 항상 자물쇠 크기 이하
# 0 : 홈부분, 1: 돌기부분

# 위치 체크해서 회전 및 이동 해야할지 여부 따지기
