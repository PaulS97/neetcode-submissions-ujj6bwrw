class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        for i in nums:
            storage[i] = storage.get(i, 0) + 1
        
        to_sort = []
        for key, value in storage.items():
            to_sort.append([value, key])

        to_sort.sort(reverse=True)
        
        final = []
        for i in range(k):
            final.append(to_sort[i][1])

        return final




        