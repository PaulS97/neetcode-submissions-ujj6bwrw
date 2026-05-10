# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        track = []
        self.inorderTraversalHelper(root, track)
        return track
    
    def inorderTraversalHelper(self, root, track):
        if root is None:
            return

        self.inorderTraversalHelper(root.left,track)
        track.append(root.val)
        self.inorderTraversalHelper(root.right,track)

        