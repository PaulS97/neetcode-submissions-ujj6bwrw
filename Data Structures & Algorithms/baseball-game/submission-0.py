class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            match operation:
                case '+':
                    stack.append(stack[-1]+stack[-2])
                case 'D':
                    stack.append(int(stack[-1])*2)
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(operation))
        
        return sum(stack)
                