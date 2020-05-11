# 정렬과 우선순위큐를 이용하여 nlogn 의 시간복잡도로 풀이
# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공

import heapq

# 입력받기
n = int(input())
arr = []
hq = []

# 데드라인 기준 정렬
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()  # 오름차순 정렬

# 최적 해 구하기
for i in arr:
    heapq.heappush(hq, i[1])    # 일단 모든 원소 heap에 push
    if i[0] < len(hq):          # heap의 크기가 데드라인(i[0]) 초과하는 경우
        heapq.heappop(hq)       # 최소 원소 제거
print(sum(hq))
