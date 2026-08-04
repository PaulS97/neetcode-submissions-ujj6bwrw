class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        store = {}

        def helper(nums, target, i):
            if i>=len(nums):
                if target==0:
                    return 1
                else:
                    return 0

            if (target, i) in store:
                return store[(target, i)]
            else:
                res = helper(nums, target-nums[i], i+1) + helper(nums, target+nums[i], i+1)
                store[(target,i)] = res
                return res

        return helper(nums, target, 0)
            

