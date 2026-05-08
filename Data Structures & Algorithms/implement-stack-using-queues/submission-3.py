class MyStack:

    def __init__(self):
        self.normal = deque()
        self.reverse = deque()

    def push(self, x: int) -> None:
        self.normal.append(x)

    def pop(self) -> int:
        for i in range(len(self.normal)-1):
            self.reverse.append((self.normal.popleft()))
        hold = self.normal.popleft()
        for i in range(len(self.reverse)):
            self.normal.append(self.reverse.popleft())
        self.reverse = deque()
        return hold

    def top(self) -> int:
        for i in range(len(self.normal)-1):
            self.reverse.append((self.normal.popleft()))
        hold = self.normal.popleft()
        for i in range(len(self.reverse)):
            self.normal.append(self.reverse.popleft())
        self.normal.append(hold)
        self.reverse = deque()    
        return hold


    def empty(self) -> bool:
        return len(self.normal) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()