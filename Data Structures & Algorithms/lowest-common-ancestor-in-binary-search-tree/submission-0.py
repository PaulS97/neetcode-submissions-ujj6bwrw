# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        pval = p.val
        qval = q.val
        while(True):
            currval = curr.val
            
            if qval >= currval >= pval or qval <= currval <= pval:
                return curr

            if qval > currval and  pval > currval:
                curr = curr.right
            else:
                curr = curr.left
            
        