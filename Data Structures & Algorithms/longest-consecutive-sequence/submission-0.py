class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        storage = {}
        
        # create sequences lenths by start sequences of 1 and combining the lengths of
        # those sequences if a connector number appears
        for num in nums:
            print("num:", num)
            if num in storage:
                continue
            else:
                left = storage.get(num-1, 0)
                right = storage.get(num+1, 0)
                total = left + right + 1
                storage[num] = total
                i = num - 1
                while i in storage:
                    storage[i] = total
                    i -= 1
                i = num + 1
                while i in storage:
                    storage[i] = total
                    i += 1
                print("total:", total)

        maxval = 0
        for num in nums:
            maxval = max(maxval, storage[num])

        return maxval


        