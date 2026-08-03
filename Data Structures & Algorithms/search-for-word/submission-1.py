class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def valid(i,j) -> bool:
            return min(i,j) >= 0 and i<len(board) and j<len(board[0]) 

        def dfs(board, word, i, j, letter_i) -> bool:
            print(i,j)
            if letter_i == len(word):
                return True

            if not valid(i,j) or (i,j) in seen:
                return False
            
            
            letter = word[letter_i]

            if board[i][j] != letter:
                return False
            else:
                seen.add((i,j))
                for up, over in directions:
                    if dfs(board, word, i+up, j+over, letter_i+1):
                        return True
            seen.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                #print("start:",i,j)
                if dfs(board, word, i, j, 0):
                    return True

        return False
                


            
            

            
   