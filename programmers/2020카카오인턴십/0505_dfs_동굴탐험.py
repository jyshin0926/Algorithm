import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

link_dict = defaultdict(list)
need_dict = defaultdict(list)

def solution(n,path,order):
    for a,b in path:
        link_dict[a].append(b)
        link_dict[b].append(a)
    # 역방향으로 그래프 체크
    set_need_dict(0,-1)

    # order에 따라서도 역방향 체크
    for a,b in order:
        need_dict[b].append(a)
    visited = [False]*n
    recur = [False]*n

    # 0번부터 n-1번까지 방번호(노드)가 사이클에 걸리는지 체크
    for node in range(n):
        if is_cycle(node, visited, recur):
            return False
    return True

# dfs로 사이클인지 아닌지 체크
def is_cycle(node, visited, recur):
    if visited[node]:
        return True
    if recur[node]:
        return False

    visited[node] = True
    recur[node] = True

    for parent_node in need_dict[node]:
        if is_cycle(parent_node, visited, recur):
            return True
    visited[node] = False
    return False


def set_need_dict(node, parent_node):
    for next_node in link_dict[node]:
        if next_node == parent_node:
            continue
        need_dict[next_node].append(node)
        set_need_dict(next_node, node)


if __name__ == '__main__':
    for n, path, order in [(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]),
                           (9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]),
                           (9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])]:
        print(solution(n, path, order))