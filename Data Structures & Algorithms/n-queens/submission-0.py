class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        start = ["."] * n
        start = "".join(start)
        options = []

        for i in range(n):
            options.append(start[:i] + "Q" + start[i+1:])

        res = []
        prevCols = []
        prevPos = []
        allowed = [True] * n

        def calculateAllowed(i, prevPos, n) -> List[int]:
            allowed = [True] * n
            for ind, pos in enumerate(prevPos):
                #print("i:", i, "pos:", pos)
                allowed[pos] = False
                if pos - (i-ind) >= 0:
                    allowed[pos - (i-ind)] = False
                if pos + (i-ind) < n:
                    allowed[pos + (i-ind)] = False
            return allowed

        def dfs(i, allowed, n):
            if i==n:
                res.append(prevCols.copy())
            for pos in range(n):
                if allowed[pos]:
                    prevCols.append(options[pos])
                    prevPos.append(pos)
                    #print("i:", i, "prevCols", prevCols)
                    newallow = calculateAllowed(i+1, prevPos, n)
                    #print("Newallow:", newallow)
                    dfs(i+1, newallow, n)
                    prevCols.pop()
                    prevPos.pop()

        dfs(0, allowed, n)

        return res



        



        