# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        columnval = {}
        minleft = 0
        maxright = 0

        def ordertracker(root, height, width):
            nonlocal minleft
            nonlocal maxright
            if root is None:
                return

            minleft = min(minleft, width)
            maxright = max(maxright, width)
            if width in columnval:
                columnval[width].append((height, root.val))
            else:
                columnval[width] = [(height, root.val)]

            #print("col:", width, "height:", height, "root:", root.val)


            ordertracker(root.left, height+1, width-1)
            ordertracker(root.right, height+1, width+1)

        ordertracker(root, 0, 0)

        res = []

        for i in range(minleft, maxright+1):
            #print("oi:", i, columnval[i])
            col = columnval[i]
            col.sort(key = lambda x: x[0])
            #print("si:", i, columnval[i])
            column = [val[1] for val in col]
            res.append(column)

        return res




            
        


            





        