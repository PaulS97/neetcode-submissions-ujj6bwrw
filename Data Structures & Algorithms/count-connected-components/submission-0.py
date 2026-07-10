class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = [[] for _ in range(0,n)]

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        seen = set()
        components = 0

        def dfs(i):
            seen.add(i)
            for node in adjList[i]:
                if node in seen:
                    continue
                else:
                    dfs(node)

        for i in range(0,n):
            if i not in seen:
                components += 1
                dfs(i)
            else:
                continue

        return components



        