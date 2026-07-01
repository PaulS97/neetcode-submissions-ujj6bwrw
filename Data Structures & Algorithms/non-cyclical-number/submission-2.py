class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        count = 0
        while(True):
            div = 1000
            sum = 0
            seen.add(n)
            while(n>0):
                rem = n // div
                sum += rem**2
                n -= rem * div
                div //= 10
            if sum == 1:
                return True
            if sum in seen:
                return False
            n = sum
            

            
                

        