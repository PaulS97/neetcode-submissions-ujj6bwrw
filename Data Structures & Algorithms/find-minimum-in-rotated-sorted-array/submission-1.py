class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minval = min(nums[l], nums[r])

        while(l<=r):
            mid = (l+r) // 2
            midval = nums[mid]
            minval = min(midval, minval)

            print(l, r, mid)
            
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                break
            elif midval < nums[l]:
                r = mid - 1
            else:
                l = mid + 1

        return minval
            





        