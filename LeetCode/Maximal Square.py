from typing import List

# Runtime: 196 ms, faster than 81.03% of Python3 online submissions for Maximal Square.
# Memory Usage: 15.7 MB, less than 25.29% of Python3 online submissions for Maximal Square.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix); n = len(matrix[0])
       # dp = [[int(x) for x in matrix[i]] for i in range(m)]
       # print(dp)
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_size = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    max_size = max(max_size, dp[i+1][j+1])
        return max_size**2

if __name__ =='__main__':
    for x in [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
              [["0","1"],["1","0"]],
              [["0"]],[["1"]],
              [["0","1"]],
              [["1","1"],["1","1"]],
              [["1","0"],["0","0"]],
              [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]]:
        print(Solution().maximalSquare(x))

# m,n 행렬
# square로
# 1나오면 주변 체크
# matrix 1나온 곳에 한해서 memoization
