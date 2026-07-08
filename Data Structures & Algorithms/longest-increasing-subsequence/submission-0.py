class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        store = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] < nums[j]:
                    store[i] = max(store[i], store[j]+1)

        return max(store)
        

            


        
        