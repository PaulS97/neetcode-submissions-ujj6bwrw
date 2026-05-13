class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])

        fresh_count = 0

        storage = deque()
        seen = []

        for i in range(height):
            for j in range(width):
                value = grid[i][j]
                if value==1:
                    fresh_count += 1
                elif value==2:
                    storage.append([i, j])      

        if fresh_count==0:
            return 0           

        def check_index(i, j):
            return 0 <= i < height and 0 <= j < width

        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        minutes = 0
        while storage and fresh_count>0:
            print(f"minutes: {minutes}")
            print(grid)
            minutes += 1
            for i in range(len(storage)):
                r, c = storage.popleft()
                for direction in directions:
                    i, j = direction
                    a, b = r+i, c+j
                    if not check_index(a, b):
                        continue
                    value = grid[a][b]
                    if value == 2 or value==0:
                        continue
                    if value == 1:
                        grid[a][b] = 2
                        storage.append([a,b])
                        print(f"appended: {a}, {b}")
                        fresh_count -= 1

        if fresh_count == 0:
            return minutes
        else:
            return -1

            

                    



        