class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        length = len(heights)
        leftMost = [-1] * length

        stack = []

        for i in range(length):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)

        rightMost = [length] * length

        stack = []

        for i in range(length-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]

            stack.append(i)

        maxArea = 0

        for i in range(length):
            r = rightMost[i] - 1
            l = leftMost[i] + 1
            area = (r - l + 1) * heights[i]
            maxArea = max(area, maxArea)

            print("i:", i, "l: ", l, "r:", r,  "height:", heights[i])

        
        return maxArea


        
 


        