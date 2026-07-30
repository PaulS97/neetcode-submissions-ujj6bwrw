class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        #for i, num in enumerate(nums):
        #    heap.append((num, i))

        #heapq.heapify_max(heap)
        for i, num in enumerate(nums):
            heapq.heappush_max(heap, (num, i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    out = heapq.heappop_max(heap)
                output.append(heap[0][0])

        return output




        