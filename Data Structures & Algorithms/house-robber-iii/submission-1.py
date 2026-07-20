# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.robtwo(root)
        return max(res[0], res[1])

    def robtwo(self, root) -> [int, int]:
        
        if root is None:
            return [0,0]
        else:
            #print(root.val)
            left = self.robtwo(root.left)
            mleft = max(left[0], left[1])

            right = self.robtwo(root.right)
            mright = max(right[0], right[1])

            noninc = mleft+mright
            inc = max(mleft+mright, left[1]+right[1]+root.val)
            #print("inc:", inc, "noninc:", noninc)
            return [inc, noninc]
        