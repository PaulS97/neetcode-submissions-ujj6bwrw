class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        if length <= 2:
            return 0

        leftMax = [0] * length
        rightMax = [0] * length

        maxHeight = 0
        for i, val in enumerate(height):
            leftMax[i] = maxHeight
            maxHeight = max(maxHeight, val)

        maxHeight = 0
        for i, val in enumerate(height[::-1]):
            rightMax[length - 1 - i] = maxHeight
            maxHeight = max(maxHeight, val)

        volume = 0
        for i in range(len(height)):
            add = max(min(rightMax[i], leftMax[i]) - height[i], 0)
            volume += add

            #print("i:", i, "rightMax:", rightMax[i], "leftMax:", leftMax[i], "add:", add)

        return volume 


        




