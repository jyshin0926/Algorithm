# begin이 target으로 변환되는 가장 짧은 루트(depth) 찾기 위해 dfs 활용

def solution(begin, target, words):
    ans = 0
    tmp = [begin]
    visited = [0 for _ in words]

    if target not in words:
        return 0

    while tmp:
        stack = tmp.pop()
        if stack == target:
            return ans      # dfs 탐색 후 최종 answer 리턴
        for i in range(len(words)):
            cnt = 0
            for j in range(len(words[i])):
                if words[i][j] != stack[j]:
                    cnt += 1
            if cnt == 1:        # words[i] 체크해서 스펠링 하나만 다를 경우 체크
                if visited[i] == 1:  # 방문한 경우
                    continue
                else:
                    visited[i] = 1   # 방문 안 한 경
                tmp.append(words[i])
        ans += 1
    return ans


print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log']))




