class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        avail = [i+1 for i in range(n)]

        def dfs(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i==len(avail):
                return
            curr.append(avail[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res
            
        