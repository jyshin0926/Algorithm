# https://taehee-kim-dev.tistory.com/116

import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict
link_dict = defaultdict(list)   # 연결정보저장
need_dict = defaultdict(list)   # a번 노드를 방문하기 위해 방문해야할 노드들 저장


def solution(n, path, order):
    for a, b in path:
        link_dict[a].append(b)
        link_dict[b].append(a)

        # 0번 방에 유일한 입구 연결되어있으므로, 모든 방들은 방문되기 위해서 0번 방 무조건 거쳐야함
        # 따라서 0번 방부터 순서를 따져봐야함
        # 여기서 이전에 방문해야하는 방 번호인 -1은 의미없는 숫자임.
    set_need_dict(0,-1) # link에서 부모-자식관계 파악해서 방문해야할 노드 설정

    for a, b in order:
        need_dict[b].append(a)  # 추가로 주어진 order에 따라 방문해야할 노드 설정

    visited = [False]*n
    recur = [False]*n
    for i in range(n):

        # i를 시작점으로 해서 사이클이 발생한다는 건 need_dict가 방문 역방향 순에 대한 정보이므로
        # i를 방문하기 이전에 i를 방문해야한다는 뜻이 되는데
        # 이는 말이 안되고, 결국 i를 방문할 수 없다는 의미이므로
        # 모든 방을 방문할 수 없게 되니까 무조건 False를 반환
        if is_cycle(i, visited, recur):
            return False
    return True


def set_need_dict(node, parent_node):
    # node 이전에 방문해야 하는 방번호는 parent_node
    # link_dict[node]에 해당하는 값은 node와 연결되어있는 모든 방들의 번호(노드들)를 원소로 갖는 리스트
    # 이 리스트에서 node와 연결되어 있는 노드를 하나씩 꺼냄
    for next_node in link_dict[node]:
        if next_node == parent_node:
            # 만약 연결되어있는 노드가
            # node 이전에 방문해야하는 노드(parent_node)라면
            # 필요없으므로 버리고 연결되어있는 다른 노드 꺼낸다.
            continue

        # 여기로 넘어왔으면,
        # next_node는 node 이후에 방문해야 하는 노드임.
        # 이후에 방문해야 하는 노드(next_node)가 더 이상 존재하지 않으면
        # node는 리프노드(맨 아래 끝 노드)이므로 재귀가 끝나고 return 됨.
        # {next_node: [node1, node2, ...]}

        # 역방향 순서로 저장하는 과정임.
        need_dict[next_node].append(node)
        # next_node를 node로 해서 재귀호출
        set_need_dict(next_node, node)

def is_cycle(node, visited, recur):
    # dfs
    # cycle이 존재한다면 어떤 노드를 방문하기 위해 그 노드를 방문해야한다는 모순 생기므로 False 리턴
    # 예를 들어 만약 1이라는 노드가 부모 타고 올라가다가
    # 어떤 노드의 부모가 자신인 1이게 되면 사이클이 존재한다는 의미이므로
    # 모든 방을 탐방하지 못할 수도 있음
    if visited[node]:   # 현재 검사하는 방 번호가 이미 방문한 방 번호라면 사이클이 발생한 것이므로 무조건 True 반환
        return True

    # 현재 검사하는 방 번호부터 시작되는 검사(현재 방 번호 이하의 방 번호들에 대한 검사)가
    # 사이클이 발생하지 않는다고 체크되어있으면 이 이후 검사는 어차피 False(사이클이 발생하지 않음)
    if recur[node]:
        return False

    visited[node] = True # 방문했음 체크
    recur[node] = True

    # node 이전에 방문해야 하는 방 번호(parent_node)를 하나씩 꺼낸다.
    for parent_node in need_dict[node]:
        # parent_node가 사이클 생기는지 검사
        if is_cycle(parent_node, visited, recur):
            return True

    # 방문 역순의 다음 순서가 더 이상 없을 때까지 계속 dfs
    # 여기로 넘어왔으면, 현재 node부터 시작했을 때 사이클이 생기지 않음을 의미
    # 따라서 node 이후의 역순 방문은 사이클이 발생하지 않음 체크
    # 그리고 다음 dfs 검사에서 visited 재사용 위해 False로 다시 바꿔주기
    # 사이클이 발생하지 않았음(False)를 반환
    visited[node] = False
    return False





if __name__ == '__main__':
    for n, path, order in [(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]),
                           (9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]),
                           (9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])]:
        print(solution(n, path, order))


