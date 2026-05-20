class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adjList[pre[0]].append(pre[1])

        #for i in range(len(adjList)):
            #print(i, adjList[i])
        

        seen_ever = set()
        seen_run = set()

        def dfs(i: int):
            #print("i:", i, end=" ")
            #print("seen_run:", seen_run)
            if i in seen_run:
                #print(i, "seen")
                return False
            if not adjList[i]:
                #print(i, "no pres")
                return True
            seen_run.add(i)
            seen_ever.add(i)
            for val in adjList[i]:
                if dfs(val) is False:
                    return False
            seen_run.remove(i)
            return True

        for course in range(numCourses):
            if course in seen_ever:
                continue
            else:
                seen_run = set()
                #print()
                #print("dfs ", course)
                if dfs(course) is False:
                    return False
        
        return True
                




            
        
        


        