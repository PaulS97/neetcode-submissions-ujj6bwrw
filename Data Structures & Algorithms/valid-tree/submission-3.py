class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        seen = set()
        process = deque()

        seen.add(0)
        process.append([0,-1])

        last = 0
        while(process):
            curr, par = process.popleft()
            for node in adjList[curr]:
                if node==par:
                    continue
                elif node in seen:
                    return False
                else:
                    process.append([node,curr])
                    seen.add(node)

        return len(seen) == n


        

        

        





        


        
        