def dfs(node, computers, visited):
    tmp = [node]
    while tmp:
        n = tmp.pop()
        if n not in visited:
            visited.append(n)
            for i in range(len(computers[node])):
                if computers[n][i] == 1 and i not in visited:
                    tmp.append(i)


def solution(n, computers):
    ans = 0; visited = []
    for i in range(len(computers)):
        if i not in visited:
            dfs(i, computers, visited)
            ans += 1
    return ans


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.08ms, 10.1MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.43ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.26ms, 10.1MB)
# 테스트 9 〉	통과 (0.15ms, 10.2MB)
# 테스트 10 〉 통과 (0.17ms, 10.2MB)
# 테스트 11 〉 통과 (1.41ms, 10.3MB)
# 테스트 12 〉 통과 (1.19ms, 10.3MB)
# 테스트 13 〉 통과 (0.55ms, 10.1MB)