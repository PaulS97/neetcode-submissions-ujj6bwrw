class Solution:
    def numDecodings(self, s: str) -> int:
        
        store = {}

        def dfs(i):
            #print(i)
            if i in store:
                return store[i]

            if i == len(s):
                return 1 
            
            if s[i] == "0":
                return 0

            one = dfs(i+1)
            two = 0

            if i<len(s)-1:
                twodig = int(s[i:i+2])
                #print(twodig)
                if twodig <= 26:
                    two = dfs(i+2)

            store[i] = one + two

            return one + two

        count = dfs(0)
        return count

            



        