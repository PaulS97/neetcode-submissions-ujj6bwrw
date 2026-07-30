# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        line = deque()
        line.append(root)
        nodes = []

        while(line):
            curr = line.popleft()
            if curr is None:
                nodes.append("null")
            else:
                nodes.append(str(curr.val))
                line.append(curr.left)
                line.append(curr.right)
        print(",".join(nodes))

        return ",".join(nodes)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        nodes = data.split(",")
        line = deque()

        root = TreeNode(int(nodes[0]))
        line.append(root)

        i = 1
        while(line):
            top = line.popleft()
            left = nodes[i]
            i+=1
            right = nodes[i]
            i+=1

            if left == "null":
                top.left = None
            else:
                leftchild = TreeNode(int(left))
                top.left = leftchild
                line.append(leftchild)

            if right == "null":
                top.right = None
            else:
                rightchild = TreeNode(int(right))
                top.right = rightchild
                line.append(rightchild)

        return root

            






