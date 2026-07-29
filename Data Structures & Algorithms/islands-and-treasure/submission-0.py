class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height = len(grid)
        length = len(grid[0])

        seen = set()
        search = deque()

        INF = 2147483647

        def add(x,y) -> bool:
            if (x,y) in seen:
                return False
            elif min(x,y) < 0 or x>= height or y>=length:
                return False
            elif grid[x][y] != INF:
                return False
            else:
                return True


        for i in range(0, height):
            for j in range(0, length):
                if grid[i][j] == 0:
                    seen.add((i,j))
                    search.append((i,j))
        steps = -1
        #print("search:", search)
        while(search):
            steps += 1
            #print("step:", steps, "search:", search)
            for i in range(0, len(search)):
                x, y = search.popleft()
                if grid[x][y] == INF:
                    grid[x][y] = steps
                for vert, hor in ([-1, 0], [1, 0], [0, 1], [0,-1]):
                    if add(x+vert, y+hor):
                        search.append((x+vert, y+hor))
                        seen.add((x,y))




      
                                




        