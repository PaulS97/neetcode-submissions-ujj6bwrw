class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift = 0
        chill = 0
        for index, value in enumerate(nums):
            if value == val:
                shift = shift + 1
            else:
                nums[index-shift] = nums[index]
                chill = chill + 1
        
        return chill
            
