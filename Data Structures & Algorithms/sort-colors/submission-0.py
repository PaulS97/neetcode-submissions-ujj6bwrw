class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store = 3 * [0]
        for number in nums:
            store[number] += 1

        k=0
        for i in range(3):
            for j in range(store[i]):
                nums[k] = i
                k+=1
