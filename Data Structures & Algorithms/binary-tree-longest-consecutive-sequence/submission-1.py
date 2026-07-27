# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longestStreak = 0
        def helper(root, parent, streak):
            if root.val - 1 == parent:
                streak += 1
            else:
                streak = 1
            left = 0
            right = 0
            if root.left:
                left = helper(root.left, root.val, streak)
            if root.right:
                right = helper(root.right, root.val, streak)

            return max(left, right, streak)
        
        return helper(root, root.val, 1)