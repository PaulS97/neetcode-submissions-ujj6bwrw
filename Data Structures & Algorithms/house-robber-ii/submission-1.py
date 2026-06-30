class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        check1 = nums[0:-1]
        check2 = nums[1:]
        #print("check1:", check1)
        #print("check2:", check2)

        def rob_cost(values) -> int:
            if len(values) == 1:
                return values[0]
            if len(values) == 2:
                return max(values[0], values[1])

            values[1] = max(values[0], values[1])

            for i in range(2, len(values)):
                values[i] = max(values[i-1], values[i-2]+values[i])

            return values[-1]

        return max(rob_cost(check1), rob_cost(check2))

            

        