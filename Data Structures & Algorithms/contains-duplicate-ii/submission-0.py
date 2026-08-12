class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        seen = set()
        k=k+1
        for i in range(min(k,len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        back = 0
        front = k
        while(front<len(nums)):
            #print(seen, back, front)
            seen.remove(nums[back])
            if nums[front] in seen:
                return True
            seen.add(nums[front])
            front+=1
            back+=1


        return False
            
        