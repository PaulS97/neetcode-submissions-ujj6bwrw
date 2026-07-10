class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for edge in edges:
            n = max(n, edge[0], edge[1])


        adjList = [[] for _ in range(0,n+1)]

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        path = []
        seen = set()
        append = True
        end = 0

        def dfs(i, par) -> bool:
            nonlocal append
            nonlocal end
            if i in seen:
                end = i
                path.append(i)
                return True
            seen.add(i)
            for node in adjList[i]:
                if node==par:
                    continue
                res = dfs(node, i)
                if res and append:
                    path.append(i)
                    if i == end:
                        append = False
                    return True



            
        dfs(1, 0)
        print("path:", path)
        pathset = set()
        for i in range(0,len(path)-1):
            pathset.add((path[i], path[i+1]))
            pathset.add((path[i+1], path[i]))
        print("pathset:", pathset)
        finalres = []
        for i in range(len(edges)-1, -1, -1):
            if (edges[i][0], edges[i][1]) in pathset:
                finalres = edges[i]
                break

        return finalres


        