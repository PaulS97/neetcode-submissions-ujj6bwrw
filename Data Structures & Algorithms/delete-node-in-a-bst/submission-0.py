# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.right and not root.left:
                root = root.right
            elif not root.right and root.left:
                root = root.left
            else:
                max_below = self.findMin(root.right)
                root.val = max_below
                root.right = self.deleteNode(root.right, max_below)
        return root

    
    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr.val
        