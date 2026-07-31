class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        else:
            target = total // 2

        def dfs(target, i):
            if target == 0:
                return True
            if i >= len(nums) or target<0:
                return False

            return dfs(target - nums[i], i+1) or dfs(target, i+1)

        return dfs(target, 0)

        
        