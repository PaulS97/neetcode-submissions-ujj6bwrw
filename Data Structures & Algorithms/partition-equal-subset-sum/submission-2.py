class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        else:
            target = total // 2

        memo = [(target+1) * [-1] for _ in range(len(nums)+1)]

        def dfs(target, i):
            if target == 0:
                return True
            if i >= len(nums) or target<0:
                memo[i][target] = False
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            else:
                memo[i][target] = dfs(target - nums[i], i+1) or dfs(target, i+1)
                return memo[i][target]

            

        return dfs(target, 0)

        
        