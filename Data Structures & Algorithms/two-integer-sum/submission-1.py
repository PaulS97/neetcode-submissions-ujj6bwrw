class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        final = []

        for index, val in enumerate(nums):
            compliment = target - val
            if compliment in storage:
                return [storage[compliment], index]
            else:
                storage[val] = index
        
        return final