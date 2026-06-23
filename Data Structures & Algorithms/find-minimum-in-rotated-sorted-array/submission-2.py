class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minval = min(nums[l], nums[r])

        while(l<=r):
            mid = (l+r) // 2
            midval = nums[mid]
            minval = min(midval, minval)
            
            if midval > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return minval
            





        