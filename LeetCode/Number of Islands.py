# Runtime: 160 ms, faster than 22.89% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.1 MB, less than 94.57% of Python3 online submissions for Number of Islands.

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            grid[i][j] = '0'
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                dfs(nx, ny)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt


if __name__ == '__main__':
    for x in [[["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]],
            [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]]:
        print(Solution().numIslands(x))