class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        seq = 1
        while(self.arr):
            if self.arr[-1][0] > price:
                break
            else:
                front = self.arr.pop()
                seq += front[1]

        self.arr.append([price, seq])
        return seq
        
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)