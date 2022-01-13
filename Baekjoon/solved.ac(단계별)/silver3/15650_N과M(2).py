import sys

n,m = map(int, sys.stdin.readline().split())

# 백트래킹으로 풀
ret = []
def dfs():
    if len(ret) == m:
        print(*ret)
        return
    for i in range(1,n+1):
        if not ret or (ret and i > ret[-1]):
            ret.append(i)
            dfs()
            ret.pop()
dfs()



# 조합으로 풀이
# from itertools import combinations
# comb = combinations(range(1,n+1), m)
# for x in comb:
#     print(*x)

