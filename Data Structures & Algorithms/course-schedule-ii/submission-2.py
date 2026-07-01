class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adjList[pre[0]].append(pre[1])

        print(adjList)

        taken = set()
        order = []

        count = 0

        for i, adj in enumerate(adjList):
            if len(adj)==0:
                #print(i, len(adj))
                taken.add(i)
                order.append(i)
                count += 1

        

        while(count!=0):
            count=0
            print(order)
            for i, adj in enumerate(adjList):
                #print(i, adj)
                if i in taken:
                    continue
                else:
                    found = True
                    for pre in adj:
                        # print(pre)
                        
                        if pre not in taken:
                            found = False
                    if found:
                        taken.add(i)
                        order.append(i)
                        count+=1
            if len(order)==numCourses:
                    return order

        return []

        
            
        