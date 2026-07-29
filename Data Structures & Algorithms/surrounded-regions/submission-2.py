class Solution:

    def solve(self, board: List[List[str]]) -> None:
        seen = set()

        height = len(board)
        length = len(board[0])

        def valid(i,j):
            return min(i,j) >= 0 and i<height and j<length

        def dfs(x,y):
            if board[x][y]=='X':
                return
            if (x,y) in seen:
                return
            seen.add((x,y))
            for i,j in [(0,1), (0,-1), (1,0), (-1,0)]:
                a,b = x+i, y+j
                if valid(a,b):
                    if board[a][b]=='O':
                        dfs(a, b)

        
        for i in range(0, height):
            dfs(i,0)
            dfs(i, length-1)

        for j in range(0, length):
            dfs(0,j)
            dfs(height-1, j)

        for i in range(0, height):
            for j in range(0, length):
                if board[i][j] == 'O' and (i,j) not in seen:
                    board[i][j]='X'

        
    



        