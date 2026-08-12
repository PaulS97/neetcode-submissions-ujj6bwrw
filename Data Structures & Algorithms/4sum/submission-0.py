class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curr = []
        res = []
        def backtrack(i):
            if len(curr) == 4:
                if sum(curr) == target:
                    res.append(curr.copy())
            elif i == len(nums):
                return
            else:
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
                while(i+1<len(nums) and nums[i]==nums[i+1]):
                    i+=1
                backtrack(i+1)

        backtrack(0)
        return res

