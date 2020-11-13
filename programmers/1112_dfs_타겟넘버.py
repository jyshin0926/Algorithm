def solution(numbers, target):
    ans = 0
    def dfs(n, t, i):
        if i < len(n):
            n[i] *= 1
            dfs(n,t, i+1)
            n[i] *= -1
            dfs(n, t, i+1)
        elif sum(n) == t:
            nonlocal ans
            ans += 1
    dfs(numbers, target,0)
    return ans

print(solution([1,1,1,1,1],3))
print(solution([2,1,3,4,5],2))

# n개의 음이 아닌 정수가 있습니다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 음 or 양 부여해서 각 조합에서 타겟 나오는 거

# dfs는 stack or 재귀 이용 / bfs는 queue 이용
# 파이썬에서는 재귀함수 호출의 깊이제한 있으므로 주의
# 재귀함수 사용 시 종료 조건 명시할 것
# 재귀함수로 구현할 수 있는 것은 반복문으로도 구현 가능(실제 코테에서는 반복분이 좀 더 빠르게 동작하는 경우도 있음)