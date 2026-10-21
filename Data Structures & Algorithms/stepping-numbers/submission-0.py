class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        final = []

        def dfs(number):
            if number > high:
                return 
            if number >= low:
                final.append(number)
            ones = number%10
            if ones > 0:
                dfs(number*10 + number%10 - 1)
            if ones < 9:
                dfs(number*10 + number%10 + 1)

        for i in range(1,10):
            dfs(i)

        if low == 0:
            final.append(0)
        
        final.sort()
        return final


        

