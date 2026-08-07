class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        store = {}
        def recursivehelper(i, j) -> int:
            if (i,j) in store:
                return store[(i,j)]
            res =0 
            if i == len(word1):
                res= len(word2) - j
            elif j == len(word2):
                res= len(word1) - i
            elif word1[i] == word2[j]:
                res= recursivehelper(i+1,j+1)
            else:
                res= 1 + min(recursivehelper(i+1,j), recursivehelper(i,j+1), recursivehelper(i+1,j+1)) 

            store[(i,j)] = res
            return res

        return recursivehelper(0,0)

        