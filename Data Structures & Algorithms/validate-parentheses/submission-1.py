class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oc_dict = {')':'(', '}':'{', ']':'['}
        o = ['(', '{', '[']
        for char in s:
            if char in o:
                stack.append(char)
            else:
                if not stack or oc_dict[char]!=stack[-1]:
                    return False
                else:
                    stack.pop()

        if not stack:
            return True
        else: 
            return False

        