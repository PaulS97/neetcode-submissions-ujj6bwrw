# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        right_mosts = []
        storage = deque()
        storage.append(root)

        level = 0
        while(len(storage)>0):
            level += 1
            for i in range(len(storage)):
                curr = storage.popleft()
                if curr.left:
                    storage.append(curr.left)
                if curr.right:
                    storage.append(curr.right)
            right_mosts.append(curr.val)

        return right_mosts

        
        