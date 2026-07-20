# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float('-inf')

        def dfs(root) -> int:
            nonlocal res

            if root is None:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)


            res = max(root.val, root.val + leftMax + rightMax, res)

            #print("root.val:", root.val, "leftMax:", leftMax, "rightMax", rightMax, "res:", res)

            return max(root.val + leftMax, root.val + rightMax)

        dfs(root)

        return res




        
        




        