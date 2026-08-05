class Solution:
    def canJump(self, nums: List[int]) -> bool:
        store = {}

        def helper(i):
            if i==len(nums)-1:
                return True
            if i>=len(nums):
                return False
            if nums[i]==0:
                return False
            if i in store:
                return store[i]
            
            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    return True
            store[i] = False
            return False

        return helper(0)