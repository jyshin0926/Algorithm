# 일단 간단하게 생각하는 게 좋다.
# 문자열 문제

# 모든 케이스 통과
def solution(skill, skill_trees):
    ans = 0
    for val in skill_trees:
        tmp = ''.join([x for x in val if x in skill])
        if skill.startswith(tmp):
            ans += 1
    return ans

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)


# 순서 조건 미충족
def solution1(skill, skill_trees):
    ans = 0
    tmp = [[] for _ in range(len(skill_trees))]
    for i in range(len(skill_trees)):
        for j in range(len(skill)):
            target = skill[j]
            idx = -1
            while True:
                idx = skill_trees[i].find(target, idx+1)
                if idx == -1:
                    break
                tmp[i].append((target))
    for x in tmp:
        if x[0] == skill[0] and len(x) == 1:
            ans += 1
        elif len(x) == 0:
            ans += 1
        elif x[0] == skill[0] and len(x) > 1:
            for i in range(1, len(x)):
                if x[i] == skill[i]:
                    ans += 1
        else:
            pass
        return tmp, ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("CBD", ["CED"]))
print(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA', 'AQWER']))
print(solution('CBD', ['AQWER']))
