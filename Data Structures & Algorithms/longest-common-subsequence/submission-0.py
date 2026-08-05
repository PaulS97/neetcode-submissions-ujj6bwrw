class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        store = {}
        def dfshelper(i,j):
            #print(i,j)
            if i>=len(text1) or j>=len(text2):
                return 0
            if (i,j) in store:
                return store[(i,j)]

            if text1[i]==text2[j]:
                res = 1 + dfshelper(i+1,j+1)
            else:
                res = max(dfshelper(i+1,j), dfshelper(i,j+1))

            store[(i,j)] = res
            return res

        return dfshelper(0,0)

            


        