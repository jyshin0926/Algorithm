def combine2(n,k):
    results = []
    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n+1):
            elements.append(i)
            print(elements)
            dfs(elements, i+1, k-1)
            print('elements.pop():',elements.pop())
    dfs([],1,k)
    return results

from itertools import combinations
def combine(n,k):
    return list(map(list, combinations(range(1,n+1),k)))

print(combine2(4,2))
# print(combine2(1,1))
# print(combine2(5,3))