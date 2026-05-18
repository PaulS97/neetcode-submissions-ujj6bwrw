class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-num for num in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones)>1:
            weight_one = -heapq.heappop(neg_stones)
            weight_two = -heapq.heappop(neg_stones)
            if weight_one > weight_two:
                diff = weight_one - weight_two
                heapq.heappush(neg_stones, -diff)
            elif weight_two > weight_one:
                diff = weight_two - weight_one
                heapq.heappush(neg_stones, -diff)
            else:
                continue
        
        if len(neg_stones)==1:
            return -neg_stones[0]
        else:
            return 0

        