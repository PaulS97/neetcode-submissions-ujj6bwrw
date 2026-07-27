"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:

        maxD = 0

        def diameterHelp(root) -> int:
            nonlocal maxD
            if root is None:
                return 0
            
            childrenHeight = []
            for node in root.children:
                childrenHeight.append(diameterHelp(node))

            #print("Node:", root.val, "ch:", childrenHeight)

            if len(childrenHeight) == 0:
                return 0
            if len(childrenHeight) == 1:
                maxD = max(childrenHeight[0]+1, maxD)
                return 1+childrenHeight[0]
            else:
                childrenHeight.sort()
                maxD = max(2 + childrenHeight[-1] + childrenHeight[-2], maxD)
                return 1 + childrenHeight[-1]

        diameterHelp(root)
        return maxD



            
                

        