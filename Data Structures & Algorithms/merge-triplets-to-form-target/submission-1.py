class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final = [False] * 3
        for triple in triplets:
           # print(triple)
     
            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue
            for i in range(3):
                if triple[i]==target[i]:
                    final[i] = True

        return final[0] and final[1] and final[2]

        