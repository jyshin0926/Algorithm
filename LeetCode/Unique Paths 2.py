from typing import List

# Runtime: 36 ms, faster than 93.10% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.4 MB, less than 31.87% of Python3 online submissions for Unique Paths II.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
                    return 0
                if obstacleGrid[i][j] == 0:
                    if len(obstacleGrid) == 1:  # 이 조건은 안 써줘도 되긴 하는데 빼면 런타임 44ms으로 늘어남
                        return 1
                    if i==0 and j==0:
                        continue
                    if 0<=i<=m-1 and 0<=j<=n-1:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

                else:
                    if len(obstacleGrid) == 1: # 이 조건도 마찬가지로 런타임 때문에 써줌
                        return 0
                    if i==0 and j==0:
                        continue
                    if 0<=i<=m-1 and 0<=j<=n-1:
                        dp[i][j] *= dp[-1][-1]
        return dp[i][j]

if __name__=='__main__':
    for x in [[[0,0,0],[0,1,0],[0,0,0]], [[0,1],[0,0]], [[1]]]:
        print(Solution().uniquePathsWithObstacles(x))