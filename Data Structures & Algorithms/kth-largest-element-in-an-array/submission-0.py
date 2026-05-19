class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newk = len(nums) - k + 1
        
        heapq.heapify(nums)
        
        for i in range(newk):
            val = heapq.heappop(nums)

        return val
        
        