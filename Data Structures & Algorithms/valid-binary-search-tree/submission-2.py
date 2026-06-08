# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        seen_order = []

        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            seen_order.append(root.val)
            helper(root.right)


        helper(root)


        for i in range(0, len(seen_order)-1):
            if seen_order[i] >= seen_order[i+1]:
                return False



        return True




        
