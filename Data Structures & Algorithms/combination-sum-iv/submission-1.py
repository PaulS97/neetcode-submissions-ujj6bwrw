class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combos = [0] * (target+1)
        combos[0] = 1

        for i in range(1, len(combos)):
            res = 0
            for num in nums:
                if i-num>=0:
                    res += combos[i-num]
                    #print(i, num, res)
            combos[i] = res
            #print(i, res, combos)

        #for ombo in combos:
            #print(ombo)

        return combos[target]

        