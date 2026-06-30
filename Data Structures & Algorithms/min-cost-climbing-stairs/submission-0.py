class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        accum = cost.copy()
        length = len(cost)

        for i in range(2, length):
            accum[i] = accum[i] + min(accum[i-1], accum[i-2])

        return min(accum[length-1], accum[length-2])
        