# bfs

from collections import defaultdict, deque

def solution(n,edge):
    dists = {i:0 for i in range(1, n+1)}    # 노드 1과 다른 노드들 사이의 거리
    edges = defaultdict(list)               # edges[node_no] 에는 node_no 노드에 연결된 노드정보를 리스트로 담기
    for u,v in edge:
        edges[u].append(v)
        edges[v].append(u)

    # 노드 1부터 bfs 순회하며 연결된 노드 순차적 탐색
    q = deque(edges[1])
    dist = 1
    while q:
        size = len(q)
        for i in range(size):
            v = q.popleft()

            if dists[v] == 0:       # 방문하지 않은 노드일 경우
                dists[v] = dist     # 거리 입력
                for w in edges[v]:
                    q.append(w)     # 그 노드와 연결된 모드 노드들 queue에 담기

        dist += 1

    # 1로 시작해서 1로 돌아오는 거리는 불필요하므로 제거
    del dists[1]

    # 거리 중 최대값 구해서 해당 값 거리 배열 중 갯수 체
    ans = 0
    max_dist = max(dists.values())
    for i in dists.values():
        if i == max_dist:
            ans += 1
    return ans


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))