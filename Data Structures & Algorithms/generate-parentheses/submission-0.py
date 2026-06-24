class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parens = []
        res = []
        
        def helper(open: int, close: int):
            if open==0 and close==0:
                res.append("".join(parens))
            elif open == 0:
                parens.append(")")
                helper(open, close-1)
                parens.pop()
            elif open == close:
                parens.append("(")
                helper(open-1, close)
                parens.pop()
            else:
                parens.append("(")
                helper(open-1, close)
                parens.pop()
                parens.append(")")
                helper(open, close-1)
                parens.pop()

        helper(n, n)

        return res
