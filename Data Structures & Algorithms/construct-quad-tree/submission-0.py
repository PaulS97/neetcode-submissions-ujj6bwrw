"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
     return self.constructHelp(grid, [0,0], [len(grid)-1,len(grid)-1])



    def constructHelp(self, grid: List[List[int]], top, bottom, depth=7) -> 'Node':
        if top == bottom:
            return Node(grid[top[0]][top[1]],  1, None, None, None, None)
        else:
            midH = (top[0] + bottom[0])//2
            midW = (top[1] + bottom[1])//2

            topLeft = self.constructHelp(grid,    [top[0], top[1]], [midH,midW], depth-1)
            topRight = self.constructHelp(grid,   [top[0], midW+1], [midH,bottom[1]], depth-1)
            bottomLeft = self.constructHelp(grid, [midH+1, top[1]], [bottom[0],midW], depth-1)
            bottomRight = self.constructHelp(grid,[midH+1, midW+1], [bottom[0],bottom[1]], depth-1)

            if (topLeft.isLeaf and 
                topRight.isLeaf and 
                bottomLeft.isLeaf and 
                bottomRight.isLeaf and 
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topRight.val, 1, None, None, None, None)
            else:
                return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)


            


        