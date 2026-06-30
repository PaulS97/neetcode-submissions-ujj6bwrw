class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma, mi = 1, 1
        res = nums[0]

        for num in nums:

            mat = max(ma*num, num, mi*num)
            mi = min(ma*num, num, mi*num)
            ma = mat
            res = max(ma, res)


        return res



        