# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_store = []
        deck = deque()

        deck.append(root)

        while(len(deck)>0):
            level_list = []
            for i in range(len(deck)):
                curr = deck.popleft()
                level_list.append(curr.val)
                if curr.left:
                    deck.append(curr.left)
                if curr.right:
                    deck.append(curr.right)
            level_store.append(level_list)

        return level_store


        