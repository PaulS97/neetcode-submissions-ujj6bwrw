class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        def swap(i,j):
            save = nums[i]
            nums[i] = nums[j]
            nums[j] = save

        def backtrack(i):
            #print(i, nums)
            if i==len(nums):
                res.add(tuple(nums))
            for j in range(i,len(nums)):
                #if nums[j-1] != nums[j]:
                swap(i,j)
                backtrack(i+1)
                swap(i,j)

        backtrack(0)

        return list(res)


