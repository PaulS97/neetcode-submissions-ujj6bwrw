class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            elif token == '+':
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                c = b / a
                if c > 0:
                    c = math.floor(c)
                else:
                    c = math.ceil(c)

                stack.append(c)

        return stack[0]


        
        