class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        finalsolution = self.subsetswo0(nums)
        finalsolution.append([])
        return finalsolution
        
    def subsetswo0(self, nums) -> List[List[int]]:
        solution = []
        if len(nums)==1:
            solution.append(nums)
            return solution

        subsetSolution = self.subsetswo0(nums[1:])
        extra_val = nums[0]
        solution.append(nums[0:1])
        for subset in subsetSolution:
            solution.append(subset + [extra_val])
            solution.append(subset)

        return solution


        
        

        




        