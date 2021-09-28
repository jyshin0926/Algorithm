graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

# 재귀함수 dfs
def recursive_dfs(v, discovered=[]):
    global graph
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w)
    return discovered


# 스택 활용 반복구조로 dfs 구현
def iterative_dfs(start_v):
    global graph
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

recursive_dfs(1)
iterative_dfs(1)

