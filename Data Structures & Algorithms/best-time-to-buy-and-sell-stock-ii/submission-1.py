class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minum = prices[0]
        profit = 0

        for price in prices:
            #print(price, minum, profit)
            if price>minum:
                profit += price - minum
                minum = price
            else:
                minum = price

        return profit

        