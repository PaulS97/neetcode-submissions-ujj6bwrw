class Solution:
    def partition(self, s: str) -> List[List[str]]:

        attempt = []
        res = []

        def isPalindrome(s, i, j) -> bool:
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        #count = 0
        def dfs(s, i, j):
            #nonlocal count
            #count +=1
            #if count > 10:
             #   return
            #print(i, j)
            #print(attempt)
            if i == len(s):
                res.append(attempt.copy())
            if j== len(s):
                return

            if isPalindrome(s, i, j):
                attempt.append(s[i:j+1])
                dfs(s, j+1, j+1)
                attempt.pop()
            dfs(s,i,j+1)

        dfs(s, 0, 0)

        return res


        

               