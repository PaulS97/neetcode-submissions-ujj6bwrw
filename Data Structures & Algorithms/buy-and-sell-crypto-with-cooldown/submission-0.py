class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store = {}
        def dfs(i, prev) -> int:
            if i>=len(prices):
                return 0
            if (i,prev) in store:
                return store[(i, prev)]
            
            if prev==-1:
                res =  max(dfs(i+1, prices[i]), dfs(i+1,-1))
                store[(i,prev)] = res
                return res
            else:
                res = max(prices[i]-prev + dfs(i+2, -1), dfs(i+1, prev))
                store[(i,prev)] = res
                return res

        return dfs(0,-1)

            # if i have a copin I can sell and skip to 2 days from now, or I can hold on to it and move to the enxt day
            # if i dont have a coin I buy and move on to the next day or I can move to the next day without buying

        