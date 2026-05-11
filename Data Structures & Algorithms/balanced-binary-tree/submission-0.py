# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True        
        balanced = abs(self.treeHeight(root.left) - self.treeHeight(root.right))<=1
        if not balanced:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)

    def treeHeight(self, root: Treenode) -> int:
        if root is None:
            return 0
        else:
            return max(self.treeHeight(root.right), self.treeHeight(root.left)) + 1

         


        