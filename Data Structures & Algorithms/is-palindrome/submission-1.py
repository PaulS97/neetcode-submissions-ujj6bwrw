class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i<=j:
            left = s[i].lower()
            right = s[j].lower()
            print(left, right)
            if not left.isalnum():
                i+=1
            elif not right.isalnum():
                j-=1
            elif left==right:
                i += 1
                j -= 1
            else:
                return False
            

        return True

        