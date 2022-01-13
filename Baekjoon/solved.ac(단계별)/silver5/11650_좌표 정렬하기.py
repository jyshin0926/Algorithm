# 정렬
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr += list(map(int, sys.stdin.readline().split())),

arr.sort(key=lambda x:(x[0],x[1]))
for p in arr:
    print(*p)