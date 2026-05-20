class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        saved_sum = [0] * len(nums)
        saved_sum[0] = nums[0]
        saved_sum[1] = max(nums[0], nums[1])

        for index, val in enumerate(nums[2:]):
            saved_sum[index+2] = max(val + saved_sum[index], saved_sum[index+1])
            #print(index, ":", saved_sum)

        return saved_sum[-1]