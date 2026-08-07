class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def invalid(i,j):
            if min(i,j) < 0 or i>=len(grid) or j>=len(grid[0]):
                return True
            else:
                return False
        seen = set()
        def dfs(i,j) -> int:
            perim = 0
            directions = ((1,0), (-1,0), (0,1), (0,-1))
            if invalid(i,j):
                return 1
            elif grid[i][j] == 0:
                return 1
            elif (i,j) in seen:
                return 0
            else:
                seen.add((i,j))
                for a,b in directions:
                    perim += dfs(i+a,j+b)
                return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)

            
        