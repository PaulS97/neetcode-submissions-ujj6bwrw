class Solution:
    def integerBreak(self, n: int) -> int:
        threes = n // 3
        rem = n%3

        if n==2:
            return 1
        if n==3:
            return 2

        if rem == 2:
            return pow(3,threes) * 2
        elif rem == 0:
            return pow(3,threes)
        else:
            return pow(3,threes-1) * 4

            
        