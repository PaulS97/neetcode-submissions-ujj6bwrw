# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        def closestValueHelper(root, target):
            nonlocal closest
            if root is None:
                return
            else: 
                if abs(target - root.val) < abs(target - closest):
                    closest = root.val
                if root.val > target:
                    closestValueHelper(root.left, target)
                else:
                    closestValueHelper(root.right, target)
        closestValueHelper(root, target)

        return closest
        