# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if head is None:
            new_node.next = new_node
            return new_node

        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head

        start = head
        prev = head
        curr = head.next

        while(True):
            prev_val = prev.val
            curr_val = curr.val

            if prev_val <= insertVal <= curr_val:
                break
            elif prev_val > curr_val:
                if insertVal >= prev_val or insertVal <= curr_val:
                    break
            elif curr == start:
                break
            prev = curr
            curr = curr.next


        prev.next = new_node
        new_node.next = curr

        if insertVal <= start.val:
            return new_node
        else:
            return start
        
