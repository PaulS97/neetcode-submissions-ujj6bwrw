class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        highest = 0

        while(l<=r):
            mid = (l+r) // 2

            need = (mid * (mid+1)) // 2

            if n>need:
                highest = mid
                l = mid+1
            elif n < need:
                r = mid - 1
            else:
                return mid

        return highest

        