class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = []
        found = 0
        seen = []

        def dfs(r, c):
            if min(r,c) < 0:
                return False
            if r >= len(grid):
                return False
            if c >= len(grid[0]):
                return False
            if [r,c] in seen:
                return False
            if grid[r][c] == "0":
                return False
            
            seen.append([r,c])

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and [i,j] not in seen:
                    found +=1
                    dfs(i,j)




        return found

                
        