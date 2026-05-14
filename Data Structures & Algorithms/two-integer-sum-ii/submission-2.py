class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(target, left, right) -> int:
            while(left<=right):
                print("target:", target)
                mid = (left + right) // 2
                print("left:", left, "right:", right, "mid:", mid)
                val = numbers[mid]
                if val == target:
                    return mid
                elif val < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1

        for index, num in enumerate(numbers):
            compliment = target - num
            compliment_id = binary_search(compliment, 0, len(numbers)-1)
            if compliment_id == -1:
                continue
            else:
                return([index+1, compliment_id+1])

        return([0,0])




        