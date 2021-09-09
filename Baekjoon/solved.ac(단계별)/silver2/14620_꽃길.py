# N 제한이 10이고 10x10 = 100, 꽃3개니까 100x100x100 = 백만
# 이 정도의 시간복잡도면 전수조사 + 방향벡터로 풀면 됨

N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

ans = 10000

# 이 문제의 경우는 방향성이 중요하지 않으므로 시계방향, 반시계방향으로 신경써서 안 써줘도 됨
# 가만히 있는 경우도 추가해주기
dx,dy= [0, 0,0,1,-1],[0, 1,-1,0,0]

# 꽃 3개 있을 때의 비용 구하는 함수
def ck(lst):
    ret = 0
    flow_tmp = []

    # 전수조사로 받아온 꽃들의 x,y좌표 구해주기
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y ==0 or y == N-1:
            return 10000   # 안 되는 케이스는 max값으로 리턴

        for w in range(5):
            # 각각의 좌표평면인 걸 set으로 하기 위해 튜플로 append해주기
            flow_tmp.append((x+dx[w],y+dy[w]))
            ret += ground[x+dx[w]][y+dy[w]]
    if len(set(flow_tmp)) != 15:
        return 10000
    return ret


# 원래대로라면 각각의 x,y를 따로 돌면서 6중 for문이 될 수 있지만
# 전수조사로 한다면 3중 for문 가능(NxN 판에서 꽃 3개를 i, j, k로 각각 받음)
for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck([i,j,k]))

print(ans)




# dx, dy = [0,1,0,-1],[1,0,-1,0]

# min_cost = 10*6; cnt = 0; tmp = []
# while cnt < 3:
#     if cnt >=3:
#         break
#     for i in range(1,N-1):
#         for j in range(1,N-1):
#             leaves = []
#             for k in range(4):
#                 ii,jj = i+dx[k], j+dy[k]
#                 leaves.append(ground[ii][jj])
#
#             min_cost = min(min_cost, ground[i][j]+sum(leaves))
#             if min_cost == ground[i][j]+sum(leaves):
#                 central = [min_cost,[i,j]]  # 가장 비용 최소가 되는 중심값 먼저 구하기
#
#             if len(tmp) == 0:
#                 tmp.append(central[1])
#             elif i == tmp[-1][0] and j == tmp[-1][1]:
#                 continue
#             else:
#                 tmp.append(central[1])
#     cnt += 1
#
#
#
# print(tmp,cnt)