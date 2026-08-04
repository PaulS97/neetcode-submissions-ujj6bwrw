class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenbig = 1
        big = s[0]


        def checkPalindrome(i, s):
            nonlocal lenbig
            nonlocal big

            j = i
            k = i
            while j>=0 and k<len(s):
                if s[j]!=s[k]:
                    break
                else:
                    j-=1
                    k+=1
            if k-j-1>lenbig:
                lenbig = k-j-1
                big = s[j+1:k]

            if i<len(s)-1 and s[i]==s[i+1]:
                j = i
                k = i+1
                while j>=0 and k<len(s):
                    if s[j]!=s[k]:
                        break
                    else:
                        j-=1
                        k+=1
                if k-j-1>lenbig:
                    lenbig = k-j-1
                    big = s[j+1:k]

        for i in range(len(s)):
            #print(i)
            checkPalindrome(i, s)

        return big
            

        