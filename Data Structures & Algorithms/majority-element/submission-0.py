class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}
        maj = len(nums) // 2

        for num in nums:
            store[num] = store.get(num, 0) + 1

        for key, value in store.items():
            if value > maj:
                return key

        