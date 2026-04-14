class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = 0
        prelim = 0
        for i in nums:
            if i == 1:
                prelim = prelim + 1
                if prelim > final:
                    final = prelim
            else:
                prelim = 0

        return final
            

        