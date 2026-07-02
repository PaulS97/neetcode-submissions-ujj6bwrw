# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        
        def findLeavesHelp(root, curr):
            if root.left and root.right:
                root.left = findLeavesHelp(root.left, curr)
                root.right = findLeavesHelp(root.right, curr)
            elif root.right:
                root.right = findLeavesHelp(root.right, curr)
            elif root.left:
                root.left = findLeavesHelp(root.left, curr)
            else:
                curr.append(root.val)
                return None
            return root

        while(root.left or root.right):
            curr=[]
            findLeavesHelp(root, curr)
            final.append(curr)

        final.append([root.val])

        return final


        