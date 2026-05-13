class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])

        if grid[0][0]==1 or grid[height-1][width-1]==1:
            return -1

        
        def valid_indices(r, c):
            return 0 <= r < height and 0 <= c < width

        directions = [-1, 0, 1]
        storage = deque()
        storage.append([0,0])

        length = 0
        while storage:
            length += 1
            for i in range(len(storage)):
                curr = storage.popleft()
                r = curr[0]
                c = curr[1]


                if r==height-1 and c==width-1:
                    return length

                if grid[r][c] == 1:
                    continue
                grid[r][c] = 1

                for i in directions:
                    for j in directions:
                        if valid_indices(r+i, c+j):
                            storage.append([r+i, c+j])

        return -1
                
                


                        



        

