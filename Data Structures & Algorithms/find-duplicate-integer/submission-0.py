class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while(i<len(nums)):
            num = nums[i]
            if num == -1:
                i += 1
            elif nums[num] == -1:
                return num
            else:
                save = nums[num]
                nums[num] = -1
                nums[i] = save
