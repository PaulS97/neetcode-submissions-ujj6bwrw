class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reverse_arr = arr[::-1]
        max_val = reverse_arr[0]
        for index in list(range(1,len(reverse_arr))):
           curr = reverse_arr[index]
           reverse_arr[index] = max_val
           max_val = max(curr, max_val)

        reverse_arr[0]=-1
        arr = reverse_arr[::-1]
        return arr
            


        