class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        length = len(heights)
        width = len(heights[0])

        pacificset = set()
        atlanticset = set()

        for i in range(0,length):
            pacificset.add((i, 0))
            atlanticset.add((i,width-1))

        for i in range(0,width):
            pacificset.add((0, i))
            atlanticset.add((length-1, i))

        alist = list(atlanticset)
        plist = list(pacificset)

        def valid(i,j):
            return i>=0 and j>=0 and i<length and j<width
                

        def dfs(i, j, oset):

            #print("i:", i, "j:", j)
            directions = [[-1, 0], [1,0], [0,1], [0,-1]]

            for k, l in directions:
                newi = i+k
                newj = j+l
                if valid(newi, newj):
                    if (newi, newj) in oset:
                        continue 
                    else:
                        if heights[i][j] <= heights[newi][newj]:
                            oset.add((newi, newj))
                            dfs(newi, newj, oset)

        for coord in alist:
            #print("start a")
            dfs(coord[0], coord[1], atlanticset)
        for coord in plist:
            #print("start p")
            dfs(coord[0], coord[1], pacificset)

        res = []
        for i in range(0, length):
            for j in range(0, width):
                if (i,j) in atlanticset and (i,j) in pacificset:
                    res.append([i,j])

        return res

        

        


        