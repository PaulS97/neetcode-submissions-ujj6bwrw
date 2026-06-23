class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while(l<=r):
            m = (l+r) // 2

            if target > nums[m]:
                if nums[r] < nums[m] or nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
            elif target < nums[m]:
                if nums[l] > nums[m] or nums[l] <= target:
                    r = m -1
                else:
                    l = m + 1
            else:
                return m

        return -1

        