class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        i=0


        while(i < len(nums)-2 and nums[i] <= 0):
            j = i + 1
            k = len(nums)-1
            while(j<k):
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    new_set = nums[i], nums[j], nums[k]
                    if not final:
                        final.append(new_set)
                    elif new_set != final[-1]:
                        final.append(new_set)
                    j += 1
                    k -= 1
            i += 1
            while(i < len(nums) - 2 and nums[i] == nums[i-1]  ):
                i += 1
        return final 

