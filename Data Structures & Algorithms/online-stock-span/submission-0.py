class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        self.arr.append(price)
        seq = 0
        for i in range(len(self.arr)-1, -1, -1):
            if price < self.arr[i]:
                break
            else:
                seq+=1

        return seq
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)