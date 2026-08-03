# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def search(val, root)->bool:
            if root is None:
                return False
            if val==root.val:
                return True
            elif val>root.val:
                return search(val, root.right)
            else:
                return search(val, root.left)

        def inorderSearch(target, root1, root2)-> bool:
            if root1 is None:
                return False
            val = target - root1.val
            center = search(val, root2)
            right = inorderSearch(target, root1.right, root2)
            left = inorderSearch(target, root1.left, root2)
            
            if center or right or left:
                return True
            else:
                return False

        return inorderSearch(target, root1, root2)

        
        
        