# start (1,1)부터 finish (m,n)까지 가는 가능한 모든 수
# 점화식 : dp[i][j] = dp[i][j-1] + dp[i-1][j]

# Runtime: 28 ms, faster than 84.10% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.3 MB, less than 66.26% of Python3 online submissions for Unique Paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if 0 <=i<=m and 0<=j<=n:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[i][j]


if __name__=='__main__':
    for a,b in [(3,7),(3,2),(7,3),(3,3)]:
        print(Solution().uniquePaths(a,b))
