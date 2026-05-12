class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        length = len(grid)
        width = len(grid[0])
    
        def dfs(r,c) -> int:
            if min(r,c) < 0:
                return 0
            if r >= length:
                return 0
            if c >= width:
                return 0
            val = grid[r][c]

            if val==0:
                return 0

            if val==1:
                grid[r][c] = 0
                up = dfs(r+1,c)
                down = dfs(r-1,c)
                right = dfs(r,c+1)
                left = dfs(r,c-1)
                return 1 + up + down + right + left

        max_island = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_island = max(max_island, area)

        return max_island



