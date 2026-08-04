class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        board = [[False]*length for _ in range(length)]

        count = 0

        for i in range(length, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j-i <= 2 or board[i+1][j-1]==True):
                    board[i][j] = True
                    count += 1
        #print(board)
        return count
    

        