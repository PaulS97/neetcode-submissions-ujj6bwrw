class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0
        zero_index = 0

        for index, i in enumerate(nums):
            if i == 0:
                zero_count += 1
                zero_index = index
            else:
                total_prod *= i

        if zero_count >= 2:
            return len(nums) * [0]

        if zero_count == 1:
            final = len(nums) * [0]
            final[zero_index] = total_prod
            return final

        final = []
        for i in nums:
            final.append(total_prod//i)

    
        return final
        