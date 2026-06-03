class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = prices[0]
        profit = 0

        for price in prices:
            if price > maxp:
                maxp = price
                if maxp - minp > profit:
                    profit = maxp - minp
            elif price < minp:
                minp = price
                maxp = price

        return profit
        