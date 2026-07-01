# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0
        def helper(root):
            nonlocal res
            if root is None:
                return 0, 0
            else:
                ls, lc = helper(root.left)
                rs, rc = helper(root.right)
                count = 1 + lc + rc
                summ = root.val + ls + rs
                av = summ/count
                #print(root.val, summ, av)
                res = max(res, av)
                return summ, count

        helper(root)
        return res

        