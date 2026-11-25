class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        intervals = []
        if nums[0] != lower:
            intervals.append([lower, nums[0]-1])
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                intervals.append([nums[i]+1, nums[i+1]-1])
        
        if nums[len(nums)-1] != upper:
            intervals.append([nums[len(nums)-1]+1, upper])

        return intervals