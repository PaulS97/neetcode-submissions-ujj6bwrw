class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        store = {}

        if len(s1)+len(s2) != len(s3):
            return False

        if s1 == "" and s2==s3 or s2 == "" and s1==s3:
            return True

        def backtrack(i,j,k):
            #if i==len(s1) and j==0 or i==0 and j==len(s2):
            #    return False
            if i==len(s1) and j==len(s2):
                return True
            if (i,j,k) in store:
                return store[(i,j,k)]
            one = False
            two = False
            if i<len(s1) and s1[i]==s3[k]:
                one = backtrack(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                two = backtrack(i,j+1,k+1) 

            res = one or two
            store[(i,j,k)] = res
            return res
            
        return backtrack(0,0,0)
