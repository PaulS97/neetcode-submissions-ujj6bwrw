"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        copied_nodes = {}

        prev = None
        curr = head
        count = 0

        while(curr):
            new_node = Node(curr.val)
            copied_nodes[curr] = new_node
            if count > 0:
                prev.next = new_node
            else:
                save = new_node
            prev = new_node
            curr = curr.next
            count += 1

        new_curr = save
        old_curr = head
        while(old_curr):
            if not old_curr.random:
                new_curr.random = None
            else:
                new_curr.random = copied_nodes[old_curr.random]
            new_curr = new_curr.next
            old_curr = old_curr.next

        return save

        

        
        