class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        storage = [width * [0] for num in range(height)]
       
        def memo_dfs(i: int, j: int):
            #print(i, j)

            if i > height-1 or j > width-1:
                #print("oob")
                return 0
            elif obstacleGrid[i][j] == 1:
                #print("blocked")
                return 0
            elif storage[i][j] > 0:
                #print("stored")
                return storage[i][j]
            elif i==height-1 and j==width-1:
                #print("end")
                return 1
            else:
                #print("continue")
                val = memo_dfs(i+1, j) + memo_dfs(i, j+1)
                #print("stored: ", val, "in", i, j, end="")
                storage[i][j] = val
                return val
            
        return memo_dfs(0, 0)


                


        