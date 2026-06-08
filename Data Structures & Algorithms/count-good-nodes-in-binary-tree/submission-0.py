# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0

        def dfs(root, maxVal)->int:
            if root is None:
                return 0
            returnVal = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            return returnVal + dfs(root.left, maxVal) + dfs(root.right, maxVal)

        
        good_count = dfs(root, root.val)

        return good_count

        