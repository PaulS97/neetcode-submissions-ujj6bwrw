class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        store = {}
        def helper(i, ex) -> int:
            if i == len(costs):
                return 0
            minval = float("inf")
            if (i, ex) in store:
                return store[(i,ex)]
            for j, cost in enumerate(costs[i]):
                if j==ex:
                    continue
                else:
                    minval = min(minval, cost + helper(i+1,j))
            store[(i,ex)] = minval

            return minval

        return helper(0,-1)



        