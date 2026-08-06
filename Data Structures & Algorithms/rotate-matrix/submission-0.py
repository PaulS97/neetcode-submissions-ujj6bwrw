class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                #print(i,j)
                save = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = save
        out = n
        #print(matrix)
        for i in range(n):
            for j in range(out):
                #print(i,j, "->", n-1-j, n-1-i)
                save = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = save
            out-=1

        #print(matrix)