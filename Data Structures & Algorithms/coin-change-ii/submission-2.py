class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        store = {}
        def helper(amount, coins, i) -> int:
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if (amount, i) in store:
               return store[(amount, i)]
            count = 0
            for j in range(i, len(coins)):
                coin = coins[j]
                count += helper(amount-coin, coins, j)
                store[(amount, i)] = count
            #print("amount:", amount, "count:", count)
            return count

        return helper(amount, coins, 0)

                


        