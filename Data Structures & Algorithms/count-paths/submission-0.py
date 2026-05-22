class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = n * [0]
        prevRow[n-1] = 1
        for i in range(m):
            currRow = n * [0]
            currRow[n-1] = 1
            for j in range(n-2, -1, -1):
                currRow[j] = currRow[j+1] + prevRow[j]
            prevRow = currRow
            print(i, ":", prevRow)

        return currRow[0]
        