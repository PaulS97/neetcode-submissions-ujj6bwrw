class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        turns = 0
        if len(nums)==1:
            return 0
        while(pos<=len(nums)-1):
            print(pos)
            step = 0
            if pos+nums[pos] >= len(nums)-1:
                return turns+1
            for i in range(pos+1, pos+nums[pos]+1):
                if nums[i]+i>step:
                    step = nums[i]+i
                    pos = i
            turns += 1

        return turns
        