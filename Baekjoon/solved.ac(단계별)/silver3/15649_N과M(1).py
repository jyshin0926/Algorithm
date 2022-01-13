import sys
n, m = map(int, sys.stdin.readline().split())

# 백트래킹으로 풀이
visited = []
ret = []  # 스택

def dfs():
    if len(ret) == m:   # ret 길이가 m 되면 출력
        print(*ret)
        return
    for i in range(1,n+1):
        if i not in ret:
            ret.append(i)
            dfs()
            ret.pop()
dfs()



# 순열로 풀이
from itertools import permutations
# permute = permutations(range(1,n+1),m)
# for x in permute:
#     print(*x)

