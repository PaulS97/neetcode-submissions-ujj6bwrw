class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, attempt):
            if i>=len(nums):
                return
            value = nums[i]
            attempt.append(value)
            print(f"attempt: {attempt}")
            sum_attempt = sum(attempt)
            if sum_attempt == target:
                res.append(attempt.copy())
            elif sum_attempt > target:
                return
            else:
                dfs(i, attempt.copy())
                attempt.pop()
                dfs(i+1, attempt.copy())

        dfs(0,[])
        return res
            


        