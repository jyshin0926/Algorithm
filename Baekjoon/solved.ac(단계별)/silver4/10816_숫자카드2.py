import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
ans = [0]*m


# 카운터로 풀이
cnt = Counter(cards)
for i in range(m):
    if target[i] in cnt:
        ans[i] = cnt[target[i]]
print(*ans,sep=' ')







