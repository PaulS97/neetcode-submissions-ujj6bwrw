# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final = []

        def dfs(root, final):
            if root is None:
                return
            dfs(root.left, final)
            final.append(root.val)
            dfs(root.right, final)

        dfs(root, final)

        return final[k-1] 

            

        

        
        



        