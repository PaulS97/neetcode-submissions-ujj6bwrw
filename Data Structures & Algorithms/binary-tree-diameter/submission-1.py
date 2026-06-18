# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dim = 0

        def sideoftree(root):
            nonlocal max_dim
            if root is None:
                return 0

            left = sideoftree(root.left)
            right = sideoftree(root.right)

            max_dim = max(left+right, max_dim)

            return max(left, right) + 1
        
        sideoftree(root)

        return max_dim

