# dfs로 풀기
def subsets2(nums):
    result = []
    def dfs(idx, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 dfs
        for i in range(idx, len(nums)):
            dfs(i+1,path+[nums[i]])

    dfs(0,[])
    return result



# combinations로 풀기
from itertools import combinations
def subsets(nums):
    ans =[]
    for i in range(len(nums)+1):
        ans += (list(map(list,combinations(nums,i))))
    return ans

print(subsets2([1,2,3]))
print('[]+[1] =',[]+[1])