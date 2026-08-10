class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        front = -1
        back = 0
        length = len(nums)+1 

        while(front<len(nums)):
            print(back, front, total)
            if total < target:
                front += 1
                try:
                    total += nums[front]
                except IndexError:
                    continue
            elif total >= target:
                length = min(length, front-back+1)
                total -= nums[back]
                back += 1

        if length == len(nums)+1:
            return 0
        else:
            return length
            

        