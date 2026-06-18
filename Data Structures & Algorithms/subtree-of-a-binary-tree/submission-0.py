# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSubtreeFlag(root, subRoot, original):
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if original:
                if (root.val == subRoot.val and 
                    isSubtreeFlag(root.right, subRoot.right, False) and
                    isSubtreeFlag(root.left, subRoot.left, False)):
                        return True
                else: 
                    return isSubtreeFlag(root.right, subRoot, True) or isSubtreeFlag(root.left, subRoot, True)
            else:
                if root.val == subRoot.val:
                    return (isSubtreeFlag(root.right, subRoot.right, False) and
                    isSubtreeFlag(root.left, subRoot.left, False))
                else:
                    return False

        return isSubtreeFlag(root, subRoot, True)



        
        