class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(nums, i, j):
            hold = nums[i]
            nums[i] = nums[j]
            nums[j] = hold

        def dfs(nums, i) :
            #print(nums, i )
            if i==len(nums):
                res.append(nums.copy())
                return
            for index in range(i, len(nums)):
                swap(nums, i, index)
                dfs(nums, i+1)
                swap(nums, i, index)

        dfs(nums, 0)

        return res




        









        