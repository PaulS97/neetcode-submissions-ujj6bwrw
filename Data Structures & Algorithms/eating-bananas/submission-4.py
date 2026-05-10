class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        works = right
        mid = (left + right) // 2

        while left<=right:
            mid = (left + right) // 2
            result = self.will_it_work(piles, h, mid)
            if result == "works":
                works = mid
                right = mid-1
            else:
                left = mid + 1

        return works



    def will_it_work(self, piles, hours, mid):
        eating_time = 0
        for bannanas in piles:
            eating_time += math.ceil(bannanas / mid)

        if eating_time <= hours:
            return "works"
        elif eating_time > hours:
            return "too_slow"
            

        
            



        