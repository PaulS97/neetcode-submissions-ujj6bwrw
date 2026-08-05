class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        length = 0
        maxsum = float("-Inf")
        maxlength = 0
        curr = 0

        for num in nums:
            curr += num
            length+=1
            if num>curr:
                curr = num
                length = 1
            if curr>maxsum:
                maxsum = curr
                maxlength = length
            #print(num, maxsum, maxlength)
            

        return maxsum
            

