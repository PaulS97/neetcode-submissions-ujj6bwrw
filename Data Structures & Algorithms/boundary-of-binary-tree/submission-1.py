# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        if root.right is None and root.left is None:
            return [root.val]
        def leftboundary(root):
            nonlocal final
            if root.right is None and root.left is None:
                return
            final.append(root.val)
            if root.left:
                leftboundary(root.left)
            else:
                leftboundary(root.right)
        def rightboundary(root):
            nonlocal final
            if root.right is None and root.left is None:
                return
            elif root.right:
                rightboundary(root.right)
            else:
                rightboundary(root.left)
            final.append(root.val)

        def getleaves(root):
            nonlocal final
            if root is None:
                return
            getleaves(root.left)
            if root.left is None and root.right is None:
                final.append(root.val)
            getleaves(root.right)

        final.append(root.val)
        if root.left:
            leftboundary(root.left)
        getleaves(root)
        if root.right:
            rightboundary(root.right)

        return final




        
        