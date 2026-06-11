class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        max_height = 0

        while(i<j):
            i_height = heights[i]
            j_height = heights[j]

            height = (j-i) * min(i_height, j_height)

            max_height = max(max_height, height)

            if i_height <= j_height:
                i += 1
            else:
                j -= 1

        return max_height

            
        