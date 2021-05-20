from typing import List

# Runtime: 512 ms, faster than 59.07% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 18.5 MB, less than 80.75% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]; stack = []
        for i in range(len(temperatures)):
            st = temperatures[i]
            while stack and temperatures[stack[-1]] < st:
                end = stack.pop()
                ans[end] = i-end
            stack.append(i)
        return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
