import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [-n for n in nums]
        heapq.heapify(self.max_heap)
        
    def add(self, val: int) -> int:
        store = []
        heapq.heappush(self.max_heap, -1*val)
        for i in range(self.k):
            store.append(heapq.heappop(self.max_heap))

        store.sort(reverse = True)
        print("store: ", store)
        res = store[0]

        for num in store:
            heapq.heappush(self.max_heap, num)

        return -1*res



        
