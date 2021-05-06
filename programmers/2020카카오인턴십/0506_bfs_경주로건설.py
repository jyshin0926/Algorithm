import math
from collections import deque
def solution(board):
    length = len(board)
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    ans = math.inf
    queue = deque()
    queue.append((0,0,-1,0))    # x좌표 y좌표 방향 비용
    visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0}
    while queue:
        x,y,way,cost = queue.popleft()
        for d in range(4):
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                new_cost = cost

                # 가장 처음에는 방향없으므로(-1) 비용에 100 추가
                if way == -1:
                    new_cost += 100

                # 기존 방향과 진행 방향이 평행한 경우
                elif (way-d) % 2 == 0:
                    new_cost += 100

                # 기존 방향과 진행 방향이 수직인 경우
                else:
                    new_cost += 600

                # 목적지에 도착했을 경우 정답값과 비교하여 더 작은 것으로 정답값 갱신
                if nx == length-1 and ny == length-1:
                    ans = min(ans, new_cost)

                # 기존에 방문하지 않았거나 방문했을 때보다 비용이 적을 경우에만 큐에 넣음
                elif visit.get((nx,ny,d)) is None or visit.get((nx,ny,d)) > new_cost:
                    visit[(nx,ny,d)] = new_cost
                    queue.append((nx,ny,d,new_cost))
    return ans

if __name__ == '__main__':
    for x in [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
              [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
              [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]:
        print(solution(x))

# visit = {(0,0,0):0, (0,0,1):2, (0,0,2):0, (0,0,3):0}
#
# print(0%2)
# print(-1%2)
# print(-2%2)
# print(-3%2)
#
# print(visit.get((0,0,0)))