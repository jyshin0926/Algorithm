from typing import List

# sol3 조회구조 개선(코드 간결화) # 성능차이는 별로 차이없음
def sol4(nums, target):
    nums_map = {}
    for i, v in enumerate(nums):
        if target-v in nums_map and i != nums_map[target-v]:
            return [i, nums_map[target-v]]
        nums_map[v] = i

# 딕셔너리는 해시테이블로 구현되어있고 조회는 평균적으로 O(1)에 가능
# 최악의 경우에는 O(n)이 될 수 있지만 매우 드물고, 분할 상환 분석에 따른 시간복잡도는 O(1)
# 따라서 이 코드는 전체적으로는 O(n)의 시간복잡도이므로 아래 코드들의 시간복잡도인 O(n^2)보다 훨씬 빠름
# Runtime: 56 ms, faster than 88.52% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 41.78% of Python3 online submissions for Two Sum.
def sol3(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장해서 두번째 수의 인덱스를 키로 즉시 조회가능하도록 함
    for i, num in enumerate(nums):
        nums_map[num] = i
    # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map and i != nums_map[complement]:
            return [i,nums_map[target-num]]
print(sol3(nums = [2,7,11,15], target = 9))
# print(sol3(nums = [3,3], target = 6))
# print(sol3(nums = [3,2,3], target = 6))

# Runtime: 648 ms, faster than 36.66% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 92.38% of Python3 online submissions for Two Sum.
def sol2(nums, target):
    # 브루트포스랑 같은 시간복잡도라도 in 연산이 더 가볍고 빠름
    # in은 파이썬 내부함수로 구현된 거라서, 파이썬 레벨에서 매번 값을 비교하는 것에 비해 훨씬 더 빨리 실행되기 때문
    for i, v in enumerate(nums):
        complement = target-v  # 모든 조합을 비교하지 않고, target에서 첫번째 값을 뺀 값이 존재하는지 탐색
        if complement in nums[i+1:]:
            return [nums.index(v), nums[i+1:].index(complement)+(i+1)]
print(sol2(nums = [2,7,11,15], target = 9))
# print(sol2(nums = [3,3], target = 6))
# print(sol2(nums = [3,2,3], target = 6))

# 브루트포스
# Runtime: 3996 ms, faster than 25.47% of Python3 online submissions for Two Sum.
# Memory Usage: 14.7 MB, less than 92.38% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
# print(Solution().twoSum(nums = [2,7,11,15], target = 9))
# print(Solution().twoSum(nums = [3,3], target = 6))
# print(Solution().twoSum(nums = [3,2,3], target = 6))