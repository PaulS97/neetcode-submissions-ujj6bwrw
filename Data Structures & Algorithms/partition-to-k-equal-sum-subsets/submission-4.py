class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        partSize = total // k

        nums.sort(reverse=True)

        parts = [0] * k

        def backtrack(i):
            #print(parts)
            if i ==len(nums):
                return True
            for p in range(k):
                #used = set()
                #if nums[p] in used:
                #    continue
                #used.add(nums[p])
                if parts[p] + nums[i] > partSize:
                    continue
                else:
                    parts[p] = parts[p] + nums[i]
                    if backtrack(i+1):
                        return True
                    parts[p] = parts[p] - nums[i]
                    if parts[p]==0:
                        break
            return False

        return backtrack(0)

                

        