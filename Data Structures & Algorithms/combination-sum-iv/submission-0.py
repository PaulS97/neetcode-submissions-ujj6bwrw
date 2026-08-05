class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        store = {}
        def helper(target):
            if target<0:
                return 0
            if target==0:
                return 1
            if target in store:
                return store[target]

            res = 0
            for num in nums:
                res += helper(target-num)
            store[target] = res

            return res
        return helper(target)
            

        