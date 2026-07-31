# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return 0
        def countHelper(root, parent) -> bool:
            nonlocal count
            if root is None:
                return True
            #print(root.val)
            left = countHelper(root.left, root.val)
            right = countHelper(root.right, root.val)

            if left and right:
                count += 1
                if root.val == parent:
                    return True
                else:
                    return False

        countHelper(root, root.val)

        return count
            


        
            

            


        