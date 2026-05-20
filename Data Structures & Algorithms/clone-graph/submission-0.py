"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        newNode = Node(node.val)

        #lookup for other nodes
        storage = {}
        storage[1] = newNode
        #store next nodes to process
        step = deque()
        step.append(node)

        while step:
            curr = step.popleft()
            curr_copy = storage[curr.val]
            for neighbor in curr.neighbors:
                if neighbor.val not in storage:
                    storage[neighbor.val] = Node(neighbor.val)
                    step.append(neighbor)
                curr_copy.neighbors.append(storage[neighbor.val])

        return storage[1]
        

                
                






